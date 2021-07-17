from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# SQLALCHAMY_DATABASE_URL = 'mysql+pymysql://root:bds316@127.0.0.1:3306/gv'
SQLALCHAMY_DATABASE_URL = 'mysql+pymysql://root:@127.0.0.1:3306/test'

engine = create_engine(SQLALCHAMY_DATABASE_URL, echo=False, pool_recycle=1200, pool_size=120)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
