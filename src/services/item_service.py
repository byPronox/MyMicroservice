from typing import List
from src.interfaces.i_item_service import IItemService
from src.interfaces.i_item_repository import IItemRepository
from src.models.item_model import Item
import logging

class ItemService(IItemService):
    def __init__(self, repository: IItemRepository):
        self.repository = repository

    def get_all_items(self) -> List[Item]:
        try:
            items = self.repository.fetch_all()
            logging.info("Service: fetched all items")
            return items
        except Exception as e:
            logging.error("Service error fetching items: %s", e)
            raise

    def add_item(self, item: Item) -> Item:
        try:
            created = self.repository.save(item)
            logging.info("Service: added item %s", created)
            return created
        except Exception as e:
            logging.error("Service error adding item: %s", e)
            raise
