from typing import List
from src.interfaces.i_item_repository import IItemRepository
from src.models.item_model import Item

class ItemRepository(IItemRepository):
    def __init__(self):
        self.items = []

    def fetch_all(self) -> List[Item]:
        return self.items

    def save(self, item: Item) -> Item:
        self.items.append(item)
        return item
