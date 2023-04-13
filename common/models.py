from database.pg_connections import product_base
from sqlalchemy import String, Boolean, Text, Integer, Column, \
    DateTime, ForeignKey, MetaData


class Products(product_base):
    __tablename__ = "products"  # noqa
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    name_new = Column(String(255), nullable=False)

