# Running the project locally

## Dependencies

If you plan on running this project only through GitHub actions,
nothing needs to be installed.

If you want to run the project locally,
the following need to be installed:

- [git](https://git-scm.com/)
- [GitHub CLI (`gh`)](https://cli.github.com/)
- [GNU Make](https://www.gnu.org/software/make/)
- [GNU Tar](https://www.gnu.org/software/tar/)
- [ImageMagick](https://imagemagick.org/index.php)
- [Nox](https://nox.thea.codes/en/stable/)
- [Python](https://www.python.org/)

## Running the project

If the [needed depdendencies](#dependencies) are installed,
you can run

```console
% nox --tags=build
```

to build the docset locally.
and

```console
% nox --tags=contribute
```

To contribute the built docset.
These are the exact commands that are ran on GitHub actions.
