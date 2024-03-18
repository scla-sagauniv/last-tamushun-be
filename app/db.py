from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine

DB_URL = "mysql+pymysql://tester:password@127.0.0.1:3306/test?charset=utf8"

engine = create_engine(DB_URL, echo=True)
session = sessionmaker(engine)

Base = declarative_base()


async def get_db():
    async with session() as session:
        yield session