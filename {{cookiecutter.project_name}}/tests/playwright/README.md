# Playwright Tests and Demos

This directory contains Playwright scripts for integration testing and interactive demos.

## Setup

1. Install dependencies: `uv sync`
2. Install Playwright browsers: `uv run playwright install`

## Running Tests

### Demo Scripts
- **Main Flow Demo**: `uv run python tests/playwright/demo_main_flow.py`
  - Demonstrates the main user journey through the application
  - Includes DOM-based annotations for clear visualization

### Integration Tests
- Run all tests: `uv run pytest tests/playwright/`
- Run specific test: `uv run python tests/playwright/test_integration.py`

## Creating New Tests

1. Copy `demo_main_flow.py` as a template
2. Update the test scenario and annotations
3. Add assertions for integration testing
4. Include comments linking to test requirements

## DOM Annotations

Use the `add_annotation()` function to add visual annotations:
```python
await add_annotation(page, "Testing login success", 50, 100)
```

## Screencast Generation

To generate screencasts for mobile review:
1. Update the demo script to save recordings
2. Use Telegram bot integration for mobile delivery
3. Store screencasts in `recordings/` directory

## Tips

- Keep annotations brief and descriptive
- Use emoji for visual appeal
- Wait for page elements to load before interactions
- Add meaningful assertions for integration tests