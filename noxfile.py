import pathlib
import shutil
from itertools import chain

import nox

HERE = pathlib.Path(__file__)
ROOT = HERE.parent


@nox.session(name="check-notebooks")
def check_notebooks(session: nox.Session) -> None:
    """Run the example notebooks."""
    session.install("-r", "requirements.txt")
    session.install("nbmake")

    args = [
        "notebooks",
        "--nbmake",
        "--nbmake-kernel=python3",
        "--nbmake-timeout=3000",
        "-vvv",
    ] + session.posargs

    session.run("pytest", *args)


@nox.session
def lint(session: nox.Session) -> None:
    """Clean lint and assert style."""
    session.install("pre-commit")
    session.run("pre-commit", "run", "--all-files")


@nox.session(python=False)
def clean(session):
    """Remove virtual environments, build files, and caches."""
    shutil.rmtree(".pytest_cache", ignore_errors=True)
    for p in chain(ROOT.rglob("*.py[co]"), ROOT.rglob("__pycache__")):
        if p.is_dir():
            p.rmdir()
        else:
            p.unlink()


@nox.session(python=False)
def nuke(session):
    """Clean and also remove the .nox directory."""
    clean(session)
    shutil.rmtree(".nox", ignore_errors=True)
