from fastapi import APIRouter

from models.restaurant import restaurant

from config.db import conn,session

restaurant_route = APIRouter()

@restaurant_route.get('/')
def home():
    return {'Hola'}

@restaurant_route.get('/restaurant')
async def get_all_restaurant():
    try:
        return await session.execute(restaurant.select()).fetchall()
    except Exception as e:
        return {'Error': str(e)}
