from sqlalchemy import create_engine

from app.model.user import Base

DB_URL = "mysql+pymysql://tester:password@brachio_db:3306/test?charset=utf8"
engine = create_engine(DB_URL, echo=True)


def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_database()