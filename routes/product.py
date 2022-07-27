from fastapi import APIRouter
from sqlalchemy import select

from models.product import product
from models.menu import menu
from models.restaurant import restaurant

from config.db import conn

product_router = APIRouter()


@product_router.get('/')
def home():
    return {'Hola'}


@product_router.get('/product/{id_restaurant}')
async def get_product(id_restaurant: int):
    try:
        find_menu = await conn.execute(select(menu).where(
            menu.c.shop_id == id_restaurant)).first()
        if find_menu == None:
            return {'Error': 'No existe un menú'}
        else:
            products = await conn.execute(select(product).where(
                product.c.menu_id == find_menu[0])).fetchall()
            if len(products) > 0:
                return {'products': products}
            else:
                return {'products': []}
    except Exception as e:
        return {'Error': str(e)}


@product_router.get('/products')
async def all_products():
    try:
        data_products = []
        products = await conn.execute(product.select()).fetchall()

        if len(products) > 0:
            for data in products:
                map_response = {}
                data_menu = conn.execute(menu.select().where(
                    menu.c.id == data['menu_id'])).first()
                restaurants = conn.execute(restaurant.select().where(
                    restaurant.c.id == data_menu[1])).first()
                if data['menu_id'] == data_menu[1] or data_menu[1] == restaurants[0]:
                    map_response = {
                        'id_restaurant': restaurants[0],
                        'name_restaurant': restaurants[1],
                        'saucer': {
                            'id': data[0],
                            'name': data[1],
                            'img': data[2],
                            'description': data[3],
                            'price': float(data[4])
                        },
                    }
                    data_products.append(map_response)

            return {'products': data_products}
        else:
            return {'products': []}
    except Exception as e:
        return {'Error: ': str(e)}
