from fastapi import APIRouter

from models.restaurant import restaurant

from config.db import conn

restaurant_route = APIRouter()

@restaurant_route.get('/')
def home():
    return {'Hola'}

@restaurant_route.get('/restaurant')
async def get_all_restaurant():
    try:
        all_restaurants = await conn.execute(restaurant.select()).fetchall()
        if len(all_restaurants) > 0:
            return {'restaurants' :all_restaurants}
        else:
            return {'restaurants': []}
    except Exception as e:
        return {'Error': str(e)}
