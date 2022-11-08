import nox
from nox import Session

PYTHON = "3.10"


@nox.session(python=PYTHON)
def docs(session: Session) -> None:
    """Build the documentation."""
    session.install("--requirement=docs/requirements.txt")

    if session.interactive:
        session.run("open", "http://127.0.0.1:8000/")
        session.run("mkdocs", "serve", *session.posargs)

    else:
        session.run("mkdocs", "build")


@nox.session(python=PYTHON, name="deploy-docs")
def deploy_docs(session: Session) -> None:
    """Deploy the documentation."""
    session.install("--requirement=docs/requirements.txt")
    session.run("mkdocs", "gh-deploy", "--force")


@nox.session(python=PYTHON, name="check-types", tags=["lint"])
def check_types(session: Session) -> None:
    """Check typing with mypy."""
    session.install("mypy", "nox", "--constraint=.github/workflows/constraints.txt")
    session.run("mypy", "noxfile.py")
