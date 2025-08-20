"""Infrastructure repositories for {{cookiecutter.project_name}}"""

from abc import ABC, abstractmethod
from typing import Optional, TypeVar, Generic

# Generic entity type
TEntity = TypeVar('TEntity')
TId = TypeVar('TId')


class Repository(ABC, Generic[TEntity, TId]):
    """Base repository interface"""
    
    @abstractmethod
    def save(self, entity: TEntity) -> TEntity:
        """Save an entity"""
        pass
    
    @abstractmethod
    def find_by_id(self, entity_id: TId) -> Optional[TEntity]:
        """Find entity by ID"""
        pass
    
    @abstractmethod
    def find_all(self) -> list[TEntity]:
        """Find all entities"""
        pass
    
    @abstractmethod
    def delete(self, entity_id: TId) -> bool:
        """Delete entity by ID"""
        pass


# TODO: Add your repository implementations here
# Example:
# class InMemorySomethingRepository(Repository[SomethingEntity, str]):
#     def __init__(self):
#         self._storage: Dict[str, SomethingEntity] = {}
#     
#     def save(self, entity: SomethingEntity) -> SomethingEntity:
#         self._storage[str(entity.id)] = entity
#         return entity