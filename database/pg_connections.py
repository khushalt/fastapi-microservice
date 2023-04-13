from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# from app import settings

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:admin@localhost:5432/test_db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, pool_size=20, max_overflow=0, echo=False
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

customer_base = declarative_base(metadata=MetaData(schema="customer"))
supplier_base = declarative_base(metadata=MetaData(schema="supplier"))
product_base = declarative_base(metadata=MetaData(schema="products"))
