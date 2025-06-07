from abc import ABC, abstractmethod
from typing import List
from src.models.item_model import Item

class IItemService(ABC):

    @abstractmethod
    def get_all_items(self) -> List[Item]:
        pass

    @abstractmethod
    def add_item(self, item: Item) -> Item:
        pass
