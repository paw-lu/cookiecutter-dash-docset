import nox
from nox import Session


@nox.session()
def docs(session: Session) -> None:
    """Build the documentation."""
    session.install("--requirement=docs/requirements.txt")

    if session.interactive:
        session.run("open", "http://127.0.0.1:8000/")
        session.run("mkdocs", "serve", *session.posargs)

    else:
        session.run("mkdocs", "build")
