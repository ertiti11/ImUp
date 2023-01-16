from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

image = Table("images", meta, 
    Column("id", Integer, primary_key=True),
    Column("title", String(50)),
    Column("url", String(100))
)


meta.create_all(engine)
