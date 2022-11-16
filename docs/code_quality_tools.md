# Code quality tools

The generated project has some code quality tools set up:

- **[flake8]**
  for linting
- **[Black]**
  for autoformatting
- **[Mypy]**
  for type checking.

Both [flake8] and [black] are ran via [pre-commit].
If you have [pre-commit] installed,
run

```console
% pre-commit install
```

in the repository to install [flake8] and [black] as pre-commit hooks.
Every time you try to make a commit,
the two will be ran to check your code.

If [nox] is installed,
run

```console
nox --session=check-types
```

to check types using [Mypy].

All checks are enforced via GitHub actions on commits and pull requests.

## Disabling

Not interested in using these linters?
Delete `.github/workflows/lint.yml`
and you'll disable the GitHub actions code quality check runs.

[black]: https://black.readthedocs.io/en/stable/
[flake8]: https://flake8.pycqa.org/en/latest/
[mypy]: https://mypy.readthedocs.io/en/stable/index.html
[pre-commit]: https://pre-commit.com/
