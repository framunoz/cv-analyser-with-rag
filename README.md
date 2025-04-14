# cv-analyser-with-rag

[![Powered by Kedro](https://img.shields.io/badge/powered_by-kedro-ffc900?logo=kedro)](https://kedro.org)

## Overview

This is your new Kedro project, which was generated using `kedro 0.19.12`.

Take a look at the [Kedro documentation](https://docs.kedro.org) to get started.

## How to install dependencies

The dependencies are handled through the `pyproject.toml` file using [`uv`](https://astral.sh/blog/uv). To install `uv`, you can consult the [`uv` documentation](https://docs.astral.sh/uv/getting-started/installation/). To install the dependencies, run the following command:

```bash
uv venv
source .venv/bin/activate  # on Windows use > . .venv\Scripts\Activate.ps1
uv sync
```

The first and second lines will create and activate a virtual environment and the third will install all the necessary dependencies for the project.

If you are a developer, you can run the following command to install the optional dependencies and install the pre-commit hooks:

```bash
uv sync --all-extras
pre-commit install
```

### 🪟 Windows-specific requirements (C++ compiler)

Some dependencies in this project (e.g., `chroma-hnswlib`, required by `chromadb`) need to be compiled from source, which requires a C++ compiler on Windows.

If you're on Windows, please make sure you install the Microsoft C++ Build Tools before running `uv sync`:

- Download from: [https://visualstudio.microsoft.com/visual-cpp-build-tools/](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

- During installation, make sure to check:
    - ✅ C++ build tools
    - ✅ Windows 10 SDK
    - ✅ MSVC v14.x

Once installed, restart your terminal and re-run:

```bash
uv sync
```

If you skip this step, you may get errors like:

```
error: Microsoft Visual C++ 14.0 or greater is required
```

## How to run your Kedro pipeline

You can run your Kedro project with:

```bash
kedro run
```

## How to test your Kedro project

Have a look at the file `src/tests/test_run.py` for instructions on how to write your tests. You can run your tests as follows:

```bash
pytest
```

You can configure the coverage threshold in your project's `pyproject.toml` file under the `[tool.coverage.report]` section.


## Project dependencies

To see and update the dependency requirements for your project use `requirements.txt`. You can install the project requirements with `pip install -r requirements.txt`.

[Further information about project dependencies](https://docs.kedro.org/en/stable/kedro_project_setup/dependencies.html#project-specific-dependencies)

## How to work with Kedro and notebooks

> Note: Using `kedro jupyter` or `kedro ipython` to run your notebook provides these variables in scope: `context`, 'session', `catalog`, and `pipelines`.
>
> Jupyter, JupyterLab, and IPython are already included in the project requirements by default, so once you have run `pip install -r requirements.txt` (or `uv sync`) you will not need to take any extra steps before you use them.

### Jupyter
To use Jupyter notebooks in your Kedro project, you need to install Jupyter:

```bash
pip install jupyter
uv pip install jupyter  # if you are using uv
```

After installing Jupyter, you can start a local notebook server:

```bash
kedro jupyter notebook
```

### JupyterLab
To use JupyterLab, you need to install it:

```bash
pip install jupyterlab
uv pip install jupyterlab  # if you are using uv
```

You can also start JupyterLab:

```bash
kedro jupyter lab
```

### IPython
And if you want to run an IPython session:

```bash
kedro ipython
```

### How to ignore notebook output cells in `git`
To automatically strip out all output cell contents before committing to `git`, you can use tools like [`nbstripout`](https://github.com/kynan/nbstripout). For example, you can add a hook in `.git/config` with `nbstripout --install`. This will run `nbstripout` before anything is committed to `git`.

> *Note:* Your output cells will be retained locally.

## Package your Kedro project

[Further information about building project documentation and packaging your project](https://docs.kedro.org/en/stable/tutorial/package_a_project.html)
