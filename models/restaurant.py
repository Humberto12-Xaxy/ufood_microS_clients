from sqlalchemy import Table
from config.db import meta, engine

restaurant = Table('shop', meta, autoload =True, autoload_with = engine)