"""Data Transfer Objects for {{cookiecutter.project_name}}"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class BaseDTO:
    """Base DTO class"""
    pass


# TODO: Add your DTOs here
# Example:
# @dataclass
# class CreateSomethingInput(BaseDTO):
#     name: str
#     description: Optional[str] = None
# 
# @dataclass
# class CreateSomethingOutput(BaseDTO):
#     id: str
#     name: str
#     created_at: str