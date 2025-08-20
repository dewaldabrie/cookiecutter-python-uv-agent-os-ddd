"""Domain entities for {{cookiecutter.project_name}}"""

from dataclasses import dataclass
from typing import Optional
from uuid import UUID, uuid4


@dataclass
class BaseEntity:
    """Base entity class with common attributes"""
    id: UUID = None
    
    def __post_init__(self):
        if self.id is None:
            self.id = uuid4()


# TODO: Add your domain entities here
# Example:
# @dataclass
# class YourEntity(BaseEntity):
#     name: str
#     description: Optional[str] = None