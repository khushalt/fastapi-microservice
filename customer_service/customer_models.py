from database.pg_connections import customer_base
from sqlalchemy import String, Boolean, Text, Integer, Column, \
    DateTime, ForeignKey, MetaData


class Customer(customer_base):
    __tablename__ = "customer"  # noqa
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
