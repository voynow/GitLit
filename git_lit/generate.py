import git_lit.config as config
from datetime import datetime, timedelta
from llm_blocks import chat_utils
import requests
import tiktoken


def query_github_trending(n_repos, last_n_days, language=None):
    """Query GitHub for trending repos"""
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
            if file["size"] == 0 and file["download_url"] is None:
                continue
            file_response = requests.get(file["download_url"], headers=headers)
            file_response.raise_for_status()

            try:
                files_dict[file["path"]] = file_response.content.decode("utf-8")
            except UnicodeDecodeError:
                print(f"Skipping file {file['path']} due to UnicodeDecodeError")

    return files_dict


def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string, allowed_special="all"))
    return num_tokens


def search_for_repo(n_repos=50, last_n_days=90):
    """Search for repos on GitHub and return repo data"""
    repos = query_github_trending(
        n_repos=n_repos, last_n_days=last_n_days, language="python"
    )

    repo_data = {}
    for repo in repos:
        key = f'{repo["name"]}/{repo["owner"]["login"]}'
        
        repo_data[key] = {}
        repo_data[key] = repo
        repo_data[key]["write_date"] = datetime.now().strftime("%Y-%m-%d")
        repo_data[key]["article_publish_date"] = ""

        repo_content = get_repo_content(
            user=repo["owner"]["login"],
            repo=repo["name"],
        )
        repo_str = "\n\n".join(
            [f"{path}\n\n{content}" for path, content in repo_content.items()]
        )
        num_tokens = num_tokens_from_string(repo_str, "cl100k_base")
        repo_data[key]["num_tokens"] = num_tokens
        print(repo_data[key]['html_url'], repo_data[key]['num_tokens'])

    return repo_data


def generate_article(repo_str):
    """
    Combine two LLM-blocks chains in the follwing workflow:
    1. Outline: generate outline from repo code
    2. Article: generate article from outline and repo code
    """
    # create outline for article
    outline_chain = chat_utils.GenericChain(
        template=config.OUTLINE_TEMPLATE, model_name="gpt-4"
    )
    outline = outline_chain(repo_str=repo_str)

    # Generate article from outline and repo code
    article_chain = chat_utils.GenericChain(
        template=config.ARTICLE_TEMPLATE, model_name="gpt-4"
    )
    article = article_chain(repo_str=repo_str, outline=outline['text'])

    # join logs from chains
    consolidated_logs = outline_chain.logs + article_chain.logs

    return article['text'], consolidated_logs