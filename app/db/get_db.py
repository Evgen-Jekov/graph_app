from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL =  "sqlite:///./graph.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
sesion_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()

def get_db():
    db = sesion_local()
    try:
        yield db
    finally:
        db.close()