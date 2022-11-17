<!-- --8<-- [start:top] -->

# Cookiecutter Dash docset

A [cookiecutter] template
for automating the generation of [documentation sets](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/Documentation_Sets/010-Overview_of_Documentation_Sets/docset_overview.html#//apple_ref/doc/uid/TP40005266-CH13-SW6)
for use in [Dash] compatible API browsers using
[doc2dash]
and contributing to [Kapeli/Dash-User-Contributions].

## What is this project?

<!-- --8<-- [end:top] -->

![Demo of Dash searching docs](docs/assets/dash_demo.gif)

<!-- --8<-- [start:bottom] -->

[Dash] is an app[^1] that lets you instantly search through documentation sets offline.
[Hynek Schlawack has a great writeup on the benefits of using Dash.](https://hynek.me/articles/productive-fruit-fly-programmer/)
If you find yourself
with dozen of documentation tabs open
or repeatedly searching for the same APIs,
[Dash] might be useful for you.

[Dash] comes with a few documentation sets,
but if a library isn't included
[you can always generate your own](https://kapeli.com/docsets).[^2]
You can contribute your documentation sets to [Kapeli/Dash-User-Contributions]
to make them available to others.

However,
if you want to keep things up to date,
each time new version of a library releases
you need to:

1. Clone the library
2. Reinstall the dependencies
3. Rebuild the docs
4. Convert the docs to a Dash-compatible documentation set
5. Create a pull request for [Kapeli/Dash-User-Contributions]

This is tedious.
As a result,
many documentation sets don't keep up with their library's release.

Cookiecutter Dash docset
generates a repository that automates this process.
After generating the project
[and modifying the template in a couple of key areas](https://paw-lu.github.io/cookiecutter-dash-docset/modifying_the_project/),
you should have a repository that specifies the entire docset building process
and automatically re-runs it on [GitHub Actions] with a new release of the library.

## Project features

Upon detecting a new project release,
this project should automatically:

1. Build a new Dash documentation set
2. Contribute the docset to [Kaplei/Dash-User-Contributions]

<!-- --8<-- [end:bottom] -->

See more information
about this project's features
in the [documentation](https://paw-lu.github.io/cookiecutter-dash-docset/how_it_works/).

<!-- --8<-- [start:references] -->

[^1]:
    There are multiple alternatives as well—like
    [Zeal](https://zealdocs.org/),
    [Velocity](https://velocity.silverlakesoftware.com/),
    [Helm Dash](https://github.com/dash-docs-el/helm-dash),
    and [dasht](https://github.com/sunaku/dasht)

[^2]: Tools like [doc2dash] help automate some of the generation.

[cookiecutter]: https://github.com/cookiecutter/cookiecutter
[dash]: https://kapeli.com/dash
[doc2dash]: https://doc2dash.readthedocs.io/en/stable
[github actions]: https://github.com/features/actions
[kapeli/dash-user-contributions]: https://github.com/Kapeli/Dash-User-Contributions

<!-- --8<-- [end:references] -->

## Documentation

Read the [documentation](https://paw-lu.github.io/cookiecutter-dash-docset/)
for more information on this project.
