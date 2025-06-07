from typing import List
from src.interfaces.i_item_service import IItemService
from src.interfaces.i_item_repository import IItemRepository
from src.models.item_model import Item

class ItemService(IItemService):
    def __init__(self, repository: IItemRepository):
        self.repository = repository

    def get_all_items(self) -> List[Item]:
        return self.repository.fetch_all()

    def add_item(self, item: Item) -> Item:
        return self.repository.save(item)
