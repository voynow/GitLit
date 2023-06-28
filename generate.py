import config
from datetime import datetime, timedelta
from llm_blocks import chat_utils
import os
import requests


def get_repo_content(user, repo, path=""):
    """Recursively get all files in a repo"""
    headers = {"Authorization": f"token {config.GITHUB_TOKEN}"}
    url = f"https://api.github.com/repos/{user}/{repo}/contents/{path}"
    repo_repsone = requests.get(url, headers=headers)
    repo_repsone.raise_for_status()

    files_dict = {}
    for file in repo_repsone.json():

        if file["type"] == "dir":
            files_dict.update(get_repo_content(user, repo, file["path"]))

        elif not any(file["name"].endswith(ext) for ext in config.EXCLUDE_EXTENSIONS):
            if file["size"] == 0 and file['download_url'] is None:
                continue
            file_response = requests.get(file["download_url"], headers=headers)
            file_response.raise_for_status()

            try:
                files_dict[file["path"]] = file_response.content.decode("utf-8")
            except UnicodeDecodeError:
                print(f"Skipping file {file['path']} due to UnicodeDecodeError")

    return files_dict


def generate_article(user: str, repo: str) -> None:
    """Generate article from a GitHub repo"""

    result = get_repo_content(
        user=user,
        repo=repo,
    )
    repo_str = "\n\n".join([f"{path}\n\n{content}" for path, content in result.items()])

    article_chain = chat_utils.GenericChain(
        template=config.TEMPLATE, model_name="gpt-4"
    )
    response = article_chain(repo_str=repo_str)

    with open("output.md", "w", encoding="utf-8") as output_file:
        output_file.write(response["text"])


def query_github_trending(n_repos, last_n_days, language=None):
    """ """
    url = "https://api.github.com/search/repositories"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"Bearer {config.GITHUB_TOKEN}",
    }

    date_N_days_ago = datetime.now() - timedelta(days=last_n_days)
    query = f"created:>{date_N_days_ago.strftime('%Y-%m-%d')}"
    if language:
        query = f"{query} language:{language}"

    params = {
        "q": query,
        "sort": "stars",
        "order": "desc",
        "per_page": min(100, n_repos),
    }

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()

    data = response.json()
    return data.get("items", [])


if __name__ == "__main__":
    repos = query_github_trending(50, 30, "python")
    # generate_article("voynow", "git2doc")
