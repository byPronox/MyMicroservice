from fastapi import APIRouter, Depends, HTTPException
import logging
from src.services.item_service import ItemService
from src.repositories.item_repository import ItemRepository
from src.models.item_model import Item

router = APIRouter()

def get_service():
    repository = ItemRepository()
    return ItemService(repository)

@router.get("/items")
def get_items(service: ItemService = Depends(get_service)):
    try:
        items = service.get_all_items()
        logging.info("Fetched all items")
        return items
    except Exception as e:
        logging.error("Error fetching items: %s", e)
        raise HTTPException(status_code=500, detail="Error fetching items")

@router.post("/items")
def create_item(item: Item, service: ItemService = Depends(get_service)):
    try:
        created = service.add_item(item)
        logging.info("Created item: %s", created)
        return created
    except Exception as e:
        logging.error("Error creating item: %s", e)
        raise HTTPException(status_code=500, detail="Error creating item")
