# {{cookiecutter.project_name}}

[![Release](https://img.shields.io/github/v/release/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})](https://img.shields.io/github/v/release/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})
[![Build status](https://img.shields.io/github/actions/workflow/status/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/ci.yml?branch=main)](https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/actions/workflows/ci.yml?query=branch%3Amain)
{% if cookiecutter.codecov == 'y' -%}
[![codecov](https://codecov.io/gh/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/branch/main/graph/badge.svg)](https://codecov.io/gh/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})
{%- endif %}
[![Commit activity](https://img.shields.io/github/commit-activity/m/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})](https://img.shields.io/github/commit-activity/m/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})
[![License](https://img.shields.io/github/license/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})](https://img.shields.io/github/license/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})

{{cookiecutter.project_description}}

- **Github repository**: <https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/>
{% if cookiecutter.mkdocs == 'y' -%}
- **Documentation**: <https://{{cookiecutter.author_github_handle}}.github.io/{{cookiecutter.project_name}}/>
{%- endif %}

## Getting Started

### Prerequisites

- [Python 3.9+](https://www.python.org/downloads/)
- [uv](https://docs.astral.sh/uv/) for dependency management
- [just](https://just.systems/) for task running:
  ```bash
  curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to ~/.local/bin
  ```

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}.git
   cd {{cookiecutter.project_name}}
   ```

2. **Set up development environment**
   ```bash
   just setup
   ```
   This installs all dependencies and sets up pre-commit hooks.

3. **View available commands**
   ```bash
   just list
   ```

### Common Development Tasks

- **Run the application**
  ```bash
  uv run python -m {{cookiecutter.project_slug}}.presentation.gui
  ```

- **Run tests**
  ```bash
  just test
  ```

- **Run tests with coverage**
  ```bash
  just test-cov
  ```

- **Format code**
  ```bash
  just fmt
  ```

- **Lint code**
  ```bash
  just lint
  ```

- **Type check**
  ```bash
  just typecheck
  ```

- **Run all quality checks**
  ```bash
  just qa
  ```

{% if cookiecutter.mkdocs == 'y' -%}
- **Serve documentation locally**
  ```bash
  just doc
  ```

- **Build and deploy documentation**
  ```bash
  just doc-build
  ```
{%- endif %}

- **Build package**
  ```bash
  just build
  ```

- **Clean build artifacts**
  ```bash
  just clean
  ```

### Project Structure

This project follows Domain-Driven Design (DDD) architecture:

```
{{cookiecutter.project_slug}}/
├── domain/          # Core business logic and entities
├── application/     # Use cases and application services
├── infrastructure/  # External interfaces and data access
└── presentation/    # UI and API endpoints
```

## Releasing a new version

{% if cookiecutter.publish_to_pypi == "y" -%}

- Create an API Token on [PyPI](https://pypi.org/).
- Add the API Token to your projects secrets with the name `PYPI_TOKEN` by visiting [this page](https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/settings/secrets/actions/new).
- Create a [new release](https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/releases/new) on Github.
- Create a new tag in the form `*.*.*`.

For more details, see [here](https://fpgmaas.github.io/cookiecutter-uv/features/cicd/#how-to-trigger-a-release).
{%- endif %}

---

Repository initiated with [fpgmaas/cookiecutter-uv](https://github.com/fpgmaas/cookiecutter-uv).
