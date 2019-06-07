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

from datetime import datetime


SQLALCHEMY_DATABASE_URI = "sqlite:///./main.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False}
)
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
    creation = Column(DateTime, default=datetime.utcnow())

    def __repr__(self):
        return "<({}, {}) at {}".format(self.x, self.y, self.creation)


Base.metadata.create_all(bind=engine)
