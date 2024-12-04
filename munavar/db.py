from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE="sqlite:///./test.db"

engin=create_engine(URL_DATABASE)
sessionlocal=sessionmaker(autoflush=False,autocommit=False,bind=engin)
Base=declarative_base()

def get_db():
    db=sessionlocal()
    try:
        yield db
    finally:
        db.close()