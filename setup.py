from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="lista_tarefas",
    version="0.0.1",
    author="Marcelo William",
    author_email="marcelo.willian@live.com",
    description="Lista de tarefas",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="github.com/Marcelowil/lista_tarefas"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.11.4',
)