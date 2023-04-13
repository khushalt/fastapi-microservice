from database.pg_connections import Base
from sqlalchemy import String, Boolean, Text, Integer, Column, \
    DateTime, ForeignKey, MetaData


class Products(Base):
    __tablename__ = "products"  # noqa
    __table_args__ = {'schema': 'products'}
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    name_new = Column(String(255), nullable=False)

