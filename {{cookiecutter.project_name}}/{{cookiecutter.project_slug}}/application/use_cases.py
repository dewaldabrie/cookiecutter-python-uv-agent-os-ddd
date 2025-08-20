"""Application use cases for {{cookiecutter.project_name}}"""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

# Generic types for use case input and output
TInput = TypeVar('TInput')
TOutput = TypeVar('TOutput')


class UseCase(ABC, Generic[TInput, TOutput]):
    """Base use case interface"""
    
    @abstractmethod
    def execute(self, input_data: TInput) -> TOutput:
        """Execute the use case with given input"""
        pass


# TODO: Add your use cases here
# Example:
# class CreateSomethingUseCase(UseCase[CreateSomethingInput, CreateSomethingOutput]):
#     def __init__(self, repository: SomethingRepository):
#         self.repository = repository
#     
#     def execute(self, input_data: CreateSomethingInput) -> CreateSomethingOutput:
#         # Implementation here
#         pass