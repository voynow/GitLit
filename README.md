# GitLit: GitHub Literature Generator 📚

![GitHub](https://img.shields.io/github/license/voynow/GitLit.com)
![PyPI](https://img.shields.io/pypi/v/GitLit)
![GitHub issues](https://img.shields.io/github/issues/voynow/GitLit.com)
![GitHub forks](https://img.shields.io/github/forks/voynow/GitLit.com)
![GitHub stars](https://img.shields.io/github/stars/voynow/GitLit.com)

GitLit is a Python-based tool that generates literature from popular up-and-coming projects on GitHub. It uses GPT-4 to create articles based on the content of a repository. This tool is perfect for developers who want to understand the technical details of a project in an easy-to-read format. 🚀

## Table of Contents 📖

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)


## Usage 🛠️

To use GitLit, you need to provide the username and repository name. You can also exclude certain file extensions. Here is an example:

```python
import os
from GitLit import get_repo_content

user = "voynow"
repo = "jamievoynow.com"
token = os.environ["GITHUB_TOKEN"]
exclude_extensions = ['.jpg']

result = get_repo_content(
    user, repo, token=token, exclude_extensions=exclude_extensions
)
```

This will return a dictionary with all the files in the repository (excluding '.jpg' files) and their content.

## Contributing 🤝

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) before getting started.

## License 📄

GitLit is licensed under the MIT License. See [LICENSE](LICENSE) for more information.

## Contact 📧

If you have any questions, feel free to reach out to Jamie Voynow at [jamievoynow.com](https://jamie-voynow.herokuapp.com/).