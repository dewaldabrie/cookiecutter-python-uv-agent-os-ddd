# {{cookiecutter.project_name}}

[![Release](https://img.shields.io/github/v/release/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})](https://img.shields.io/github/v/release/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})
[![Build status](https://img.shields.io/github/actions/workflow/status/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/main.yml?branch=main)](https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/actions/workflows/main.yml?query=branch%3Amain)
[![Commit activity](https://img.shields.io/github/commit-activity/m/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})](https://img.shields.io/github/commit-activity/m/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})
[![License](https://img.shields.io/github/license/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})](https://img.shields.io/github/license/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})

{{cookiecutter.project_description}}

## Core Concept
{{cookiecutter.main_idea}}

## Key Features
{{cookiecutter.key_features}}

## Target Users
{{cookiecutter.target_users}}

## Quick Start

### Installation
```bash
# Clone or generate from template
uvx cookiecutter ~/code/cookiecutter-uv-agent-os-ddd

# Install dependencies
uv sync

# Install Playwright browsers
uv run playwright install
```

### Running the Application
```bash
# Start the NiceGUI application
uv run python -m {{cookiecutter.project_slug}}

# Or directly run the GUI module
uv run python -m {{cookiecutter.project_slug}}.presentation.gui
```

### Development
```bash
# Run tests
uv run pytest

# Type checking
uv run mypy src/

# Linting
uv run ruff check src/

# Generate documentation
uv run mkdocs serve
```

## Architecture

This project follows **Clean Architecture** with **Domain-Driven Design (DDD)**:

- **Domain Layer**: Business entities and rules
- **Application Layer**: Use cases and orchestration  
- **Infrastructure Layer**: External integrations
- **Presentation Layer**: NiceGUI user interface

See the [Architecture Overview](architecture/overview.md) for detailed information.

## Development Workflow

1. **Spec-First**: Define requirements in `.agent-os/product/` files
2. **Domain Modeling**: Start with entities and business logic
3. **Use Cases**: Implement application workflows
4. **UI Development**: Create NiceGUI components
5. **Testing**: Add unit and integration tests
6. **Documentation**: Update MkDocs with Mermaid diagrams
