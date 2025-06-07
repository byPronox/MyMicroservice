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

class ItemRepository(IItemRepository):
    def __init__(self):
        self._items = []
        self._next_id = 1

    def fetch_all(self) -> List[Item]:
        return self._items

    def save(self, item: Item) -> Item:
        item.id = self._next_id
        self._next_id += 1
        self._items.append(item)
        return item
