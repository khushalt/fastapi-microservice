from database.pg_connections import supplier_base
from sqlalchemy import String, Boolean, Text, Integer, Column, \
    DateTime, ForeignKey, MetaData


class Supplier(supplier_base):
    __tablename__ = "supplier"  # noqa
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)

