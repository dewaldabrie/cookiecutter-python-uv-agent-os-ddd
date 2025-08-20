# Project Tech Stack

{% if cookiecutter.tech_stack_preference == "default" -%}
## Core Stack (Default)
- Language: Python 3.11+
- Primary Database: PostgreSQL 17+
- ORM: SQLAlchemy
- GUI Framework: NiceGUI
- Python venv tool: Astral UV
- CSS Framework: TailwindCSS 4.0+
- Font Loading: Self-hosted for performance
- Icons: Lucide React components
- Application framework: Docker compose
- Version control: git

## Documentation Stack
- Documentation Framework: MkDocs
- Documentation Theme: mkdocs-material
- Diagram Plugin: mkdocs-mermaid2
- Diagram Types: Class, Sequence, Flowchart, ER, State diagrams

## Testing and Demo Stack
- Browser Automation: Playwright Python
- Integration Testing: Playwright scripts with DOM annotations
- Demo Generation: Screencasts via Playwright
- Testing Framework: pytest

## Development Tools
- Linting: ruff
- Type Checking: mypy
- Dependency Management: uv
- CI/CD Platform: GitHub Actions
{% else -%}
## Custom Tech Stack

<!-- Define your custom tech stack preferences here -->

### Core Technologies
- Language: 
- Database: 
- Framework: 
- Package Manager: 

### Development Tools
- Linting: 
- Type Checking: 
- Testing: 
- CI/CD: 

### Documentation
- Documentation Tool: 
- Diagram Tool: 
{% endif %}