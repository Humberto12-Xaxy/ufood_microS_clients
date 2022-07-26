from fastapi import APIRouter
from sqlalchemy import select

from models.product import product
from models.menu import menu

from config.db import conn

product_router = APIRouter()

@product_router.get('/product/{id_restaurant}')
async def get_product(id_restaurant:int):
    try:
        find_menu = conn.execute(select(menu).where(menu.c.shop_id == id_restaurant)).first()
        if find_menu == None:
            return {'Error': 'No existe un menú'}
        else:
            print(find_menu,find_menu[0])
            if find_menu[0] == None or find_menu[0] == []:
                return {'Error': 'No existe un producto'}
            else:
                products = conn.execute(select(product).where(product.c.menu_id == find_menu[0])).fetchall()
                return {'products' : products}
    except Exception as e:
        return {'Error': str(e)}