# Development Best Practices

## Context

Global development guidelines for Agent OS projects.

<conditional-block context-check="core-principles">
IF this Core Principles section already read in current context:
  SKIP: Re-reading this section
  NOTE: "Using Core Principles already in context"
ELSE:
  READ: The following principles

## Core Principles

### Keep It Simple
- Implement code in the fewest lines possible
- Avoid over-engineering solutions
- Choose straightforward approaches over clever ones

### Optimize for Readability
- Prioritize code clarity over micro-optimizations
- Write self-documenting code with clear variable names
- Add comments for "why" not "what"

### DRY (Don't Repeat Yourself)
- Extract repeated business logic to private methods
- Extract repeated UI markup to reusable components
- Create utility functions for common operations

### File Structure
- Keep files focused on a single responsibility
- Group related functionality together
- Use consistent naming conventions

### Architecture
- Always use domain driven development (DDD) and test driven development (TDD) together. Use clean architecture with separate application layer, domains and infrastructure. Let each domain have its own models. Translate between models or even better use data transfer objects (DTO) where possible. Use common design patterns like:
  * strategy pattern
  * repository pattern
  * factory pattern
  * dependency injection
  * command pattern
  * observer pattern

### Documentation-First Development
- Generate MkDocs sites for each project with clean architecture structure
- Organize documentation by clean architecture layers: domain, application, infrastructure, presentation
- Include clickable indexes linking to key files for easy navigation
- Embed Mermaid diagrams for visual clarity:
  * Class diagrams for domain entities and relationships
  * Sequence diagrams for use case interactions and API call stacks
  * Flowcharts for infrastructure workflows and presentation flows
  * ER diagrams for database schema visualization
  * State diagrams for application state transitions
- Use mkdocs-material theme and mkdocs-mermaid2 plugin
- Auto-update documentation when code changes

### Frontend Architecture Patterns
- For simple, server-side rendered apps, use MVC (Model-View-Controller):
  * Model: Data logic in the domain layer
  * View: NiceGUI templates for rendering
  * Controller: Handles requests and responses
- For interactive apps, use MVVM (Model-View-ViewModel):
  * Model: Domain layer data
  * View: NiceGUI UI components
  * ViewModel: Reactive logic for dynamic updates
- Document frontend structure with appropriate Mermaid diagrams

### Interactive Testing and Demos
- Create Playwright scripts for integration tests and user flow demos
- Include DOM-based text annotations for step-by-step walkthroughs
- Ensure scripts are runnable locally with simple commands
- Generate screencasts for remote review and mobile access
- Store test scripts in organized folder structure (tests/playwright)

### Command Runner and Development Workflow
- Use Just command runner for all development tasks to ensure consistency
- Create comprehensive justfile with commands for:
  * Development setup (`just bootstrap`, `just install`)
  * Code quality (`just fix`, `just quality`, `just pre-commit`)
  * Testing (`just test`, `just test-coverage`, `just test-watch`)
  * Documentation (`just docs-serve`, `just docs-build`)
  * Database operations (`just db-migrate`, `just db-reset`)
  * Docker operations (`just docker-up`, `just docker-down`)
  * Dependency checking (`just deps-check`)
  * Interactive testing (`just playwright`)
  * Utility (`just list`, `just version`)
- Include detailed README.md with "Getting Started" section that:
  * Lists all prerequisites (Python, UV, Just)
  * Provides step-by-step setup instructions
  * Shows essential Just commands for daily development
  * Includes troubleshooting section with common issues
  * Documents project structure and architecture principles
- Use UV for fast, reliable Python package management:
  * `uv sync` for installing project dependencies
  * `uv run` for running scripts and applications
- Ensure all development tasks are accessible through Just commands for consistency

### Configuration Consolidation
- Consolidate Python tool configurations into pyproject.toml when possible:
  * Ruff configuration (replaces ruff.toml)
  * Coverage configuration (replaces .coveragerc)
  * Pytest configuration (replaces pytest.ini)
  * MyPy configuration (replaces mypy.ini)
  * Tool-specific settings in [tool.*] sections
- Keep separate configuration files only when required by tools:
  * .pre-commit-config.yaml (pre-commit doesn't read pyproject.toml)
  * mkdocs.yml (complex nested structures work better in YAML)
  * alembic.ini (logging configuration requires INI format)
  * docker-compose.yml (Docker-specific format)
- Benefits of consolidation:
  * Single source of truth for project configuration
  * Easier maintenance and version control
  * Reduced configuration drift
  * Better discoverability of project settings
</conditional-block>

<conditional-block context-check="dependencies" task-condition="choosing-external-library">
IF current task involves choosing an external library:
  IF Dependencies section already read in current context:
    SKIP: Re-reading this section
    NOTE: "Using Dependencies guidelines already in context"
  ELSE:
    READ: The following guidelines
ELSE:
  SKIP: Dependencies section not relevant to current task

## Dependencies

### Choose Libraries Wisely
When adding third-party dependencies:
- Select the most popular and actively maintained option
- Check the library's GitHub repository for:
  - Recent commits (within last 6 months)
  - Active issue resolution
  - Number of stars/downloads
  - Clear documentation
</conditional-block>

