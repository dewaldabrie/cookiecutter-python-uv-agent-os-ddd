# Cookiecutter Agent OS DDD Template

A cookiecutter template for creating Python projects with Clean Architecture, Domain-Driven Design (DDD), and Agent OS integration.

---

[![Supported Python versions](https://img.shields.io/badge/python-3.11_%7C_3.12_%7C_3.13-blue?labelColor=grey&color=blue)](#)
[![License](https://img.shields.io/badge/license-MIT-blue)](#)

This is a modern Cookiecutter template based on [cookiecutter-uv](https://github.com/fpgmaas/cookiecutter-uv) that creates Python projects with clean architecture principles, domain-driven design, and Agent OS integration. It supports the following features:

- 🏗️ **Clean Architecture** with DDD layers (Domain, Application, Infrastructure, Presentation)
- 🎨 **NiceGUI Frontend** for Python-based UI development
- 📚 **MkDocs Documentation** with Mermaid diagrams and architecture visualization
- 🎭 **Playwright Integration** for testing and interactive demos
- 🤖 **Agent OS Integration** with product specification files
- ⚡ **UV Package Management** for fast dependency resolution
- 🧪 **Testing Setup** with pytest, mypy, and ruff
- 📊 **Comprehensive Tooling** for development workflow

---

<p align="center">
  <a href="https://fpgmaas.github.io/cookiecutter-uv/">Documentation</a> - <a href="https://github.com/fpgmaas/cookiecutter-uv-example">Example</a>
</p>

---

## Quickstart

### Prerequisites

- Python 3.11+
- [UV](https://docs.astral.sh/uv/) package manager
- [Cookiecutter](https://cookiecutter.readthedocs.io/)

### Generate a New Project

```bash
# Install cookiecutter if not already installed
uvx install cookiecutter

# Generate project from template
uvx cookiecutter ~/code/cookiecutter-uv-agent-os-ddd
```

or if you don't have `uv` installed yet:

```bash
pip install cookiecutter
cookiecutter ~/code/cookiecutter-uv-agent-os-ddd
```

### Template Prompts

The template will prompt you for:

- **Project Name**: Display name for your project
- **Project Description**: Brief description of the project
- **Main Idea**: Core concept and purpose of your project
- **Key Features**: List of main features (comma-separated)
- **Target Users**: Who will use this application and scenarios
- **Tech Stack Preference**: Choose default or custom tech stack
- **Author Information**: Your name, email, and GitHub handle

### Post-Generation Setup

The template automatically:

1. ✅ Initializes git repository
2. ✅ Sets up UV virtual environment
3. ✅ Installs dependencies
4. ✅ Installs Playwright browsers
5. ✅ Creates Agent OS product files

Follow the prompts to configure your project. Once completed, navigate into your newly created project directory and start developing!

## Project Structure

```
your-project/
├── .agent-os/product/          # Agent OS specification files
│   ├── init.md                # Project initialization details
│   ├── decisions.md           # Architecture decision records
│   ├── mission.md             # Mission statement
│   ├── mission-lite.md        # Brief mission overview
│   ├── roadmap.md             # Product roadmap
│   └── tech-stack.md          # Technology choices
├── src/your_project/           # Source code (clean architecture)
│   ├── domain/                # Business entities and rules
│   ├── application/           # Use cases and orchestration
│   ├── infrastructure/        # External integrations
│   └── presentation/          # NiceGUI user interface
├── tests/                     # Test files
│   ├── playwright/            # Browser automation tests
│   ├── unit/                  # Unit tests
│   └── integration/           # Integration tests
├── docs/                      # MkDocs documentation
│   └── architecture/          # Architecture documentation
├── pyproject.toml             # Project configuration
└── mkdocs.yml                 # Documentation configuration
```

## Development Workflow

### 1. Running the Application

```bash
cd your-project
uv run python -m your_project
```

### 2. Development Commands

```bash
# Run tests
uv run pytest

# Type checking
uv run mypy src/

# Linting and formatting
uv run ruff check src/
uv run ruff format src/

# Generate documentation
uv run mkdocs serve
```

### 3. Playwright Testing

```bash
# Run integration tests
uv run python tests/playwright/demo_main_flow.py

# Run all playwright tests
uv run pytest tests/playwright/
```

## Architecture Principles

This template follows **Clean Architecture** with **Domain-Driven Design**:

1. **Domain Layer**: Business entities and rules
2. **Application Layer**: Use cases and orchestration
3. **Infrastructure Layer**: External integrations
4. **Presentation Layer**: NiceGUI user interface

## Agent OS Integration

The template creates Agent OS product specification files to help with project planning and development:

- **init.md**: Project details from cookiecutter prompts
- **decisions.md**: Architecture decision records
- **mission.md**: Project mission and vision
- **roadmap.md**: Development roadmap
- **tech-stack.md**: Technology stack documentation

## Acknowledgements

This project is based on [Florian Maas's](https://github.com/fpgmaas) excellent [cookiecutter-uv](https://github.com/fpgmaas/cookiecutter-uv) template, extended with Agent OS integration and clean architecture principles.
