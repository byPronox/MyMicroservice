from fastapi import APIRouter, Depends
from src.services.item_service import ItemService
from src.repositories.item_repository import ItemRepository
from src.models.item_model import Item

router = APIRouter()

def get_service():
    repository = ItemRepository()
    return ItemService(repository)

@router.get("/items")
def get_items(service: ItemService = Depends(get_service)):
    return service.get_all_items()

@router.post("/items")
def create_item(item: Item, service: ItemService = Depends(get_service)):
    return service.add_item(item)
