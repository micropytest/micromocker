# micro:Mocker System Guide

## Project Overview

**micro:Mocker** is a lightweight library for mocking things on the **micro:Pytest** test framework and **MicroPython**.


## Tech stack

- **Programming language**: **MicroPython** 1.28

- **Testing**: **unittest**, **Should**

- **Dependency management**:
  [Poetry](https://python-poetry.org) is used for managing project dependencies and virtual environments.

- **Linting and formatting**: The project uses [Ruff](https://docs.astral.sh/ruff) for both high-performance linting and code formatting.
  [Pyright](https://github.com/microsoft/pyright) is also used for static type checking.


## Project structure

```
/
├───.github/              # GitHub Actions workflows and templates
├───scripts/
│   ├───install           # Dependency installation script
│   └───tests             # Test execution script
├───micromocker/          # micro:Mocker code
├───tests/                # Test directory
│   └───unit/             # Unit tests
├───manifest.py           # MicroPython metadata file
├───package.json          # MicroPython metadata file
├───.ruff.toml            # Ruff configuration file
├───pyrightconfig.json    #Pyright configuration file
├───pyproject.toml        # Project metadata and dependencies (Poetry)
├───README.md             # Project overview
└───...
```


## Development workflow and commands

All commands should be run from the project root:

- **Running Tests**.
  The primary test script executes unit tests using a **MicroPython** environment:

  ```bash
  poetry run scripts/tests
  ```

- **Linting**.
  Check the codebase for style issues and errors with **Ruff** and **Pyright**:

  ```bash
  poetry run pyright
  poetry run ruff check
  ```

- **Formatting**:
  Automatically format the code using **Ruff**:

  ```bash
  poetry run ruff format .
  ```
