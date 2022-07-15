from fastapi import FastAPI

from routes.product import product_router
from routes.restaurant import restaurant_route

app = FastAPI()

app.include_router(product_router)
app.include_router(restaurant_route)