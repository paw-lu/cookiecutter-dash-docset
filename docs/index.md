# Cookiecutter Dash docset

A [cookiecutter] template
for automating the generation of [documentation sets](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/Documentation_Sets/010-Overview_of_Documentation_Sets/docset_overview.html#//apple_ref/doc/uid/TP40005266-CH13-SW6)
for use in [Dash] compatible API browsers using
[doc2dash]
and contributing to [Kapeli/Dash-User-Contributions].

## What is this project?

![Demo of Dash searching docs](assets/dash_demo.gif)

[Dash][^1] is an app that lets you instantly search through documentation sets offline.
[Hynek Schlawack has a great writeup on the benefits of using Dash.](https://hynek.me/articles/productive-fruit-fly-programmer/)
If you find yourself
with dozen of documentation tabs open
or repeatedly searching for the same APIs,
[Dash] might be useful for you.

[Dash] comes with a few documentation sets,
but if a library isn't included
[you can always generate your own documentation set](https://kapeli.com/docsets).[^2]
To make your generated documentation sets available to others
you can contribute them to [Kapeli/Dash-User-Contributions].

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
[and modifying the template in a couple of key areas](#generating-the-project),
you should have a repository that specifies the entire docset building process
and automatically re-runs it on [GitHub Actions] with a new release of the library.

## Features

- Automates the creation of library documentation sets
- Automatically detects new library release
- Generates pull requests against dash
- Provides checks to see if build stale

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
