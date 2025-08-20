# Application Layer

The application layer orchestrates domain objects to fulfill application requirements.

## Structure

```
{{cookiecutter.project_slug}}/application/
├── __init__.py
├── use_cases.py  # Application use cases
└── dtos.py       # Data Transfer Objects
```

## Key Files

- [`use_cases.py`](../{{cookiecutter.project_slug}}/application/use_cases.py): Application use cases
- [`dtos.py`](../{{cookiecutter.project_slug}}/application/dtos.py): Data transfer objects

## Use Case Flow

```mermaid
sequenceDiagram
    participant UI as Presentation Layer
    participant UC as Use Case
    participant D as Domain Layer
    participant R as Repository
    
    UI->>UC: Execute use case
    UC->>R: Fetch entity
    R->>UC: Return entity
    UC->>D: Apply business logic
    D->>UC: Return result
    UC->>R: Save changes
    UC->>UI: Return DTO
```

## Use Case Pattern

```mermaid
classDiagram
    class UseCase~TInput, TOutput~ {
        <<abstract>>
        +execute(input: TInput): TOutput
    }
    
    %% Add your use cases here
    %% class CreateSomethingUseCase {
    %%     +repository: Repository
    %%     +execute(input: CreateInput): CreateOutput
    %% }
    
    %% UseCase <|-- CreateSomethingUseCase
```

## Design Principles

- **Single Responsibility**: One use case per business operation
- **Dependency Inversion**: Use cases depend on abstractions
- **Input/Output DTOs**: Clear data contracts
- **Transaction Boundaries**: Use cases define transaction scope

## Adding New Use Cases

1. Define input and output DTOs
2. Create use case class implementing `UseCase` interface
3. Inject required repositories/services
4. Implement business logic orchestration
5. Update sequence diagrams above