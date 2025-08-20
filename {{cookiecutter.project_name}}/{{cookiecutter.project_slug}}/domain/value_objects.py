"""Domain value objects for {{cookiecutter.project_name}}"""

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class BaseValueObject:
    """Base value object class"""
    
    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, type(self)):
            return False
        return self.__dict__ == other.__dict__


# TODO: Add your value objects here
# Example:
# @dataclass(frozen=True)
# class Email(BaseValueObject):
#     value: str
#     
#     def __post_init__(self):
#         if '@' not in self.value:
#             raise ValueError('Invalid email format')