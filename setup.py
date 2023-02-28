# for mohamad -> run this to get auto requirments.txt file in ipynb
# import session_info
# session_info.show()


# for reema and eleen use this line to install all dependency
# python setup.py install

from pathlib import Path

from setuptools import find_namespace_packages, setup

# Load packages from requirements.txt
BASE_DIR = Path(__file__).parent
with open(Path(BASE_DIR, "requirements.txt"), "r") as file:
    required_packages = [ln.strip() for ln in file.readlines()]

style_packages = ["black==22.8.0"]
analysis_packes = ["jupyterlab==3.4.6"]
docs_packages = ["mkdocs==1.3.0", "mkdocstrings==0.18.1"]
# Define our package
setup(
    name="MLOps",
    version=1.0,
    description="a test project for MLOps",
    author="your name",
    author_email="your email",
    python_requires=">=3.7",
    packages=find_namespace_packages(),
    install_requires=[required_packages],
    extras_require={
        "dev": style_packages + analysis_packes,
        "docs": docs_packages,
    },
)
