from fastapi import APIRouter

from models.restaurant import restaurant

from config.db import conn

restaurant_route = APIRouter()

@restaurant_route.get('/restaurant')
def get_all_restaurant():
    try:
        return conn.execute(restaurant.select()).fetchall()
    except Exception as e:
        return {"Error":str(e)}
        