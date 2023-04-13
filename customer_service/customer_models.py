from database.pg_connections import Base
from sqlalchemy import String, Boolean, Text, Integer, Column, \
    DateTime, ForeignKey, MetaData


class Customer(Base):
    __tablename__ = "customer"  # noqa
    __table_args__ = {'schema': 'customer'}
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
