from sqlalchemy import Table
from config.db import meta, engine

menu = Table('menu', meta, autoload =True, autoload_with = engine)