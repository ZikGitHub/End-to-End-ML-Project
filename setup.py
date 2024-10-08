import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"


REPO_NAME = "End-to-End-ML-Project"
AUTHOR_USER_NAME = "ZikGitHub"
AUTHOR_EMAIL = "XK9nK@example.com"
SRC_REPO = "mlproject"
LIST_OF_REQUIREMENTS = []


setuptools.setup(
    name=REPO_NAME,
    source_repo=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for MLops to end-to-end deployement",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)