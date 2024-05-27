import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPOSITORY_NAME = "Chicken-Disease-Classification-MLOPS"
AUTHOR_NAME = "KR-16"
SRC_REPO_NAME = "ChickenDieaseClassifier"
AUTHOR_EMAIL = "keerthirajkv2@gmail.com"

setuptools.setup(
    name=SRC_REPO_NAME,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="Python Package for Chicken Dieases Classifier",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{REPOSITORY_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPOSITORY_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)