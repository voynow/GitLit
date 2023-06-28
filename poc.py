"""
# GitLit
Github Literature generated from popular up-and-coming projects. 

Initial Proof of Concept:
- Get all files from a repo recursively
- Invoke GPT-4 with the repo's contents as input
- generate an article based on the repo's contents
"""

import requests
from llm_blocks import chat_utils
import os


def get_repo_content(user, repo, path="", token="", exclude_extensions=[]):
    """Recursively get all files in a repo"""
    headers = {"Authorization": f"token {token}"}
    url = f"https://api.github.com/repos/{user}/{repo}/contents/{path}"
    repo_repsone = requests.get(url, headers=headers)
    repo_repsone.raise_for_status()

    files_dict = {}
    for file in repo_repsone.json():
        if file["type"] == "dir":
            files_dict.update(
                get_repo_content(user, repo, file["path"], token, exclude_extensions)
            )
        elif not any(file["name"].endswith(ext) for ext in exclude_extensions):
            file_response = requests.get(file["download_url"], headers=headers)
            file_response.raise_for_status()
            files_dict[file["path"]] = file_response.content.decode("utf-8")

    return files_dict


def main():
    user = "voynow"
    repo = "jamievoynow.com"
    token = os.environ["GITHUB_TOKEN"]
    exclude_extensions = [".jpg"]

    result = get_repo_content(
        user, repo, token=token, exclude_extensions=exclude_extensions
    )
    repo_str = "\n\n".join([f"{path}\n\n{content}" for path, content in result.items()])

    template = """
    Write an article on the following repo describing its technical details for learning purposes:

    {repo_str}
    """
    article_chain = chat_utils.GenericChain(template=template, model_name="gpt-4")
    response = article_chain(repo_str=repo_str)
    print(response["text"])


if __name__ == "__main__":
    main()
