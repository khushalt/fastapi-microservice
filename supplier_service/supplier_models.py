from database.pg_connections import Base
from sqlalchemy import String, Boolean, Text, Integer, Column, \
    DateTime, ForeignKey, MetaData


class Supplier(Base):
    __tablename__ = "supplier"  # noqa
    __table_args__ = {'schema': 'supplier'}
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)

