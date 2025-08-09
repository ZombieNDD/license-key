from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class LicenseDatabase():
    def connect_database(self):
        SQLALCHEMY_DATABASE_URL = "sqlite:///./license.db"
        engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
        SessionLocal = sessionmaker(bind=engine)
        Base = declarative_base()

        return SessionLocal, Base


