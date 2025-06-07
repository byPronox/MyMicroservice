from abc import ABC, abstractmethod
from typing import List
from src.models.item_model import Item

class IItemRepository(ABC):

    @abstractmethod
    def fetch_all(self) -> List[Item]:
        pass

    @abstractmethod
    def save(self, item: Item) -> Item:
        pass
