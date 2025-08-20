# Presentation Layer

The presentation layer handles user interface and interactions using NiceGUI.

## Structure

```
{{cookiecutter.project_slug}}/presentation/
├── __init__.py
└── gui.py  # NiceGUI frontend
```

## Key Files

- [`gui.py`](../{{cookiecutter.project_slug}}/presentation/gui.py): Main NiceGUI application

## UI Architecture Pattern

The frontend uses **MVC** pattern for simple applications:

```mermaid
flowchart LR
    U[User] --> V[View<br/>NiceGUI Components]
    V --> C[Controller<br/>Event Handlers]
    C --> M[Model<br/>Domain Layer]
    M --> C
    C --> V
    V --> U
```

For interactive applications, consider **MVVM** pattern:

```mermaid
sequenceDiagram
    participant U as User
    participant V as View
    participant VM as ViewModel
    participant M as Model
    
    U->>V: User Input
    V->>VM: Data Binding
    VM->>M: Business Logic
    M->>VM: Updated Data
    VM->>V: Reactive Update
    V->>U: UI Update
```

## Application State

```mermaid
stateDiagram-v2
    [*] --> Loading
    Loading --> Ready: App Initialized
    Ready --> Processing: User Action
    Processing --> Ready: Action Complete
    Processing --> Error: Action Failed
    Error --> Ready: User Retry
    Ready --> [*]: App Closed
```

## Component Structure

```mermaid
graph TD
    A[Main Page] --> B[Header Component]
    A --> C[Content Area]
    A --> D[Footer Component]
    
    C --> E[Feature Cards]
    C --> F[User Info Panel]
    
    E --> G[Feature 1]
    E --> H[Feature 2]
    E --> I[Feature 3]
```

## Design Principles

- **Component-Based**: Reusable UI components
- **Reactive**: UI updates based on state changes
- **Responsive**: Works on different screen sizes
- **Accessible**: Follows accessibility guidelines

## Adding New UI Components

1. Create component function in appropriate module
2. Add to main page layout
3. Connect to use cases via event handlers
4. Update component diagram above
5. Add Playwright tests for user interactions