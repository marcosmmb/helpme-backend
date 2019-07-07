from sqlalchemy import (
    Boolean,
    Column,
    Integer,
    String,
    Float,
    DateTime,
    create_engine,
)
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import sessionmaker
import os

from datetime import datetime

#SQLALCHEMY_DATABASE_URI = "sqlite:///./main.db"
#SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
SQLALCHEMY_DATABASE_URI = "postgres://kvpiijfokwhwez:7b315e7343e78e277a5cfe207027339166890491829bc59f9036aaffeb9c402f@ec2-54-227-251-33.compute-1.amazonaws.com:5432/d8nbofc5oocua4"

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False}
# )
engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class CustomBase:

    id = Column(Integer, primary_key=True, index=True)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


Base = declarative_base(cls=CustomBase)


class User(Base):
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean(), default=True)
    x = Column(Float, default=0)
    y = Column(Float, default=0)

    def __repr__(self):
        return "<{} ({}, {})>".format(self.email, self.x, self.y)


class Alarm(Base):
    x = Column(Float, default=0)
    y = Column(Float, default=0)
    creation = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "<({}, {}) at {}>".format(self.x, self.y, self.creation)


Base.metadata.create_all(bind=engine)
