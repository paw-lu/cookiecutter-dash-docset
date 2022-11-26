# Generating a project

[Cookiecutter] must be installed
in order to generate this project.

??? question "How to install [cookiecutter]"

    You can install cookiecutter using [homebrew](https://brew.sh/)

    ```console
    % brew install cookiecutter
    ```

    or [pipx](https://pypa.github.io/pipx/)

    ```console
    % pipx install cookiecutter
    ```

    [Cookiecutter's documents some more detailed installation instructions.](https://cookiecutter.readthedocs.io/en/stable/installation.html#installation)

Once cookiecutter is installed,
run:

```console
% cookiecutter https://github.com/paw-lu/cookiecutter-dash-docset
```

You'll get some prompts asking you questions about the generated project:

| Variable                  | Description                                                                                                                                   | Example                          |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| `library_name`            | The name of the library you will generate a docset for.                                                                                       | `pip`                            |
| `library_repository_name` | The name of the repository on GitHub for the library. By default set equal to `library_name`.                                                 | `pip`                            |
| `repo_releases`           | How the repository records releases. Does it specifically specify releases, or does it just have tagged commits?                              | `Has releases`                   |
| `installable_name`        | The name of the installable for the library. The thing you would type in when you `pip install`. By default set to `library_repository_name`. | `pip`                            |
| `library_version`         | The version of the library to build the docs from.                                                                                            | `22.3`                           |
| `library_owner`           | The GitHub owner name of the repository for the library.                                                                                      | `pypa`                           |
| `github_username`         | Your GitHub username.                                                                                                                         | `paw-lu`                         |
| `your_name`               | Your name.                                                                                                                                    | `Paulo S. Costa`                 |
| `project_name`            | The name of the generated project. By default `{library_repository_name}-dash-docset`                                                         | `pip-dash-docset`                |
| `documentation_url`       | The url the library's documentation is hosted at.                                                                                             | `https://pip.pypa.io/en/stable/` |
| `python_version`          | The python version which will run the build script.                                                                                           | `3.10`                           |

[cookiecutter]: https://github.com/cookiecutter/cookiecutter
