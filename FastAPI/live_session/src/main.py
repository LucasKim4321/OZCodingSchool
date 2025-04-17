from fastapi import FastAPI

from user.api import router as user_router
from item.api import router as item_router

app = FastAPI()
app.include_router(user_router)
app.include_router(item_router)
