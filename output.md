# Turbo Docs: Automating Documentation with OpenAI's GPT Models

Documentation is a crucial part of any software development process. It helps developers understand the codebase, makes it easier for users to use the software, and ensures that knowledge about the code is not lost over time. However, writing and maintaining documentation can be a time-consuming task. This is where Turbo Docs comes in.

Turbo Docs is an open-source Python package that automates the generation of documentation for Python projects. It leverages the power of OpenAI's GPT models to create concise and informative documentation, making it easier for developers to understand the code and for users to use the software.

## Why Use Turbo Docs?

Turbo Docs offers several benefits over manual documentation:

- **Save time**: Turbo Docs automatically generates documentation for your Python functions, so you can focus on writing code.
- **Stay up-to-date**: Turbo Docs can be easily integrated into your development workflow, ensuring your documentation is always current.
- **High-quality documentation**: Turbo Docs leverages the power of OpenAI's GPT models to generate concise and informative documentation.
- **Customizable**: You can choose between GPT-3.5 Turbo and GPT-4 models, and even provide your own templates for generating documentation.

## How Does Turbo Docs Work?

Turbo Docs uses a combination of Python's built-in `ast` module and OpenAI's GPT models to generate documentation. The `ast` module is used to parse the Python code and identify functions, while the GPT models are used to generate the actual documentation.

The main functions of Turbo Docs are `generate_docs` and `docs`. The `generate_docs` function generates and writes documentation for a given function using the specified model and template. The `docs` function parses the code in a given repository, identifies functions within Python files, and generates documentation for each function using a specified model and template.

In addition to generating documentation for individual functions, Turbo Docs can also generate a README.md file for your project using the `readme` function. This function selects between GPT-3.5 Turbo and GPT-4, allows for template override, and generates a README.md file for the given repository.

## Using Turbo Docs

To use Turbo Docs, you first need to install it using pip:

```bash
pip install turbo_docs
```

Once installed, you can generate documentation for your Python project by navigating to your project's root directory and running:

```bash
turbo_docs --docs
```

To generate a README.md file for your project, run:

```bash
turbo_docs --readme
```

For more options, run:

```bash
turbo_docs --help
```

## Contributing to Turbo Docs

Turbo Docs is an open-source project, and contributions are welcome! If you have any improvements or suggestions, feel free to submit a pull request or open an issue to discuss them.

## Conclusion

Turbo Docs is a powerful tool that can save developers a lot of time and effort. By automating the process of generating documentation, it allows developers to focus on what they do best: writing code. If you're a Python developer, give Turbo Docs a try - it might just revolutionize your workflow!