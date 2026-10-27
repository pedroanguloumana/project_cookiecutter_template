# {{cookiecutter.project_name}}

{{cookiecutter.description}}
***

# Installation

From the project root, create and activate a Conda environment on each machine:

```sh
conda env create --name {{ cookiecutter.repo_name }} --file environment.yml
conda activate {{ cookiecutter.repo_name }}
```

Install this project's Python package in editable mode:

```sh
python -m pip install -e .
```

Add project-specific dependencies to `environment.yml` and update the environment with
`conda env update --name {{ cookiecutter.repo_name }} --file environment.yml`.
y