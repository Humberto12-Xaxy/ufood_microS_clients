from sqlalchemy import Table
from config.db import engine, meta

product = Table('saucer', meta, autoload =True, autoload_with = engine)