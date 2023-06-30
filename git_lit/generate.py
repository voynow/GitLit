import git_lit.config as config
from datetime import datetime, timedelta
import json
from llm_blocks import chat_utils
import requests
import tiktoken


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


def get_repo_content(user, repo, branch):
    """Get the content of a GitHub repo"""
    headers = {
        "Authorization": f"Bearer {config.GITHUB_TOKEN}",
        "Content-Type": "application/json",
    }
    variables = {
        "owner": user,
        "name": repo,
        "branch": branch + ":",
    }
    response = requests.post(
        "https://api.github.com/graphql",
        headers=headers,
        json={
            "query": config.GH_GQL_QUERY,
            "variables": json.dumps(variables),
        },
    )
    response.raise_for_status()
    return response.json()


def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string, allowed_special="all"))
    return num_tokens


def search_for_repo(n_repos=50, last_n_days=90):
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
            branch=repo["default_branch"],
        )
        repo_str = "\n\n".join(
            [f"{path}\n\n{content}" for path, content in repo_content.items()]
        )
        num_tokens = num_tokens_from_string(repo_str, "cl100k_base")
        repo_data[key]["num_tokens"] = num_tokens
        print(repo_data[key]['html_url'], repo_data[key]['num_tokens'])

    return repo_data


def generate_article(repo_str):
    """Generate article from a GitHub repo"""

    article_chain = chat_utils.GenericChain(
        template=config.TEMPLATE, model_name="gpt-4"
    )
    return article_chain(repo_str=repo_str)
