# {{cookiecutter.project_name}}

{{cookiecutter.description}}
***

# Installation
1. First create a new conda environment. I recommend naming the conda environment the same as the project repo name:
```
conda create -n {{ cookiecutter.repo_name }}
```

2. Activate the enviornment:
```
conda activate {{ cookiecutter.repo_name }}
```

3. Install the project package with pip:
```
cd {{ cookiecutter.project_name.lower().replace(' ', '_') }}
pip install -e . {{ cookiecutter.package_name}}
```

4. Setup the environment (note the ```source``` command):
```
source {{ cookiecutter.repo_name }}/scripts/setup_env.sh
```