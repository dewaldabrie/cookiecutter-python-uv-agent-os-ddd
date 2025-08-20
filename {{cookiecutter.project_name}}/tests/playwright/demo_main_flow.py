"""Main user flow demo script for {{cookiecutter.project_name}}

This script demonstrates the main user flow using Playwright with DOM annotations.
Run with: uv run python tests/playwright/demo_main_flow.py
"""

import asyncio
from playwright.async_api import async_playwright


async def add_annotation(page, text: str, x: int = 50, y: int = 50):
    """Add a DOM-based text annotation to the page"""
    await page.evaluate(f"""
        const annotation = document.createElement('div');
        annotation.innerHTML = '{text}';
        annotation.style.cssText = `
            position: fixed;
            top: {y}px;
            left: {x}px;
            background: rgba(0, 123, 255, 0.9);
            color: white;
            padding: 8px 12px;
            border-radius: 4px;
            font-family: Arial, sans-serif;
            font-size: 14px;
            z-index: 9999;
            box-shadow: 0 2px 8px rgba(0,0,0,0.3);
        `;
        document.body.appendChild(annotation);

        // Auto-remove after 3 seconds
        setTimeout(() => {{ "{{" }}
            if (annotation.parentNode) {{ "{{" }}
                annotation.parentNode.removeChild(annotation);
            {{ "}}" }}
        {{ "}}" }}, 3000);
    """)


async def demo_main_flow():
    """Demo the main user flow of {{cookiecutter.project_name}}"""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=1000)
        page = await browser.new_page()
        
        try:
            # Start the demo
            await add_annotation(page, "🚀 Starting {{cookiecutter.project_name}} Demo", 50, 50)
            
            # Navigate to the application (assuming it runs on localhost:8080)
            await page.goto("http://localhost:8080")
            await page.wait_for_timeout(2000)
            
            await add_annotation(page, "📱 Loading main application page", 50, 100)
            await page.wait_for_timeout(2000)
            
            # Demo key features
            features = '{{cookiecutter.key_features}}'.split(', ')
            for i, feature in enumerate(features):
                await add_annotation(page, f"✨ Feature: {feature}", 50, 150 + (i * 50))
                await page.wait_for_timeout(1500)
            
            await add_annotation(page, "🎯 Target Users: {{cookiecutter.target_users}}", 50, 300)
            await page.wait_for_timeout(2000)
            
            await add_annotation(page, "✅ Demo completed successfully!", 50, 350)
            await page.wait_for_timeout(3000)
            
        except Exception as e:
            await add_annotation(page, f"❌ Error: {str(e)}", 50, 400)
            await page.wait_for_timeout(3000)
        
        finally:
            await browser.close()


if __name__ == "__main__":
    print("🎭 Starting Playwright demo for {{cookiecutter.project_name}}")
    print("📝 Make sure your application is running on http://localhost:8080")
    print("💡 To start the app: uv run python -m {{cookiecutter.project_slug}}.presentation.gui")
    
    asyncio.run(demo_main_flow())