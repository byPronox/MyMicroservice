from fastapi import FastAPI
from src.config import config
from src.controllers import item_controller

app = FastAPI(
    title=config.APP_NAME,
    version=config.APP_VERSION
)

app.include_router(item_controller.router)
