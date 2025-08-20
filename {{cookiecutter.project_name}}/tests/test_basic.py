"""Basic tests for {{cookiecutter.project_name}}"""

from {{cookiecutter.project_slug}} import __version__


def test_version():
    """Test that version is defined"""
    assert __version__ == "0.1.0"


def test_import():
    """Test that main modules can be imported"""
    from {{cookiecutter.project_slug}}.domain import entities
    from {{cookiecutter.project_slug}}.application import use_cases
    from {{cookiecutter.project_slug}}.infrastructure import repositories
    from {{cookiecutter.project_slug}}.presentation import gui
    
    # Basic smoke test - modules should import without error
    assert entities is not None
    assert use_cases is not None
    assert repositories is not None
    assert gui is not None
