from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine

DB_URL = "mysql+pymysql://tester:password@brachio_db:3306/test?charset=utf8"

engine = create_engine(DB_URL, echo=True)
session = sessionmaker(engine)

Base = declarative_base()

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
