from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="simple-image-processing",  # Nome que será usado no PyPI
    version="0.0.1",
    author="Rafael Santiago",
    author_email="rafaelrsantiago@hotmail.com",
    description="Pacote simples para processamento de imagens usando Python.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/santoraf09/simple-image-processing-package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
