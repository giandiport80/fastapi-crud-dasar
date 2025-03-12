from sqlalchemy import Column, Integer, String, TIMESTAMP

from app.config.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    email = Column(String, nullable=True)
    password = Column(String, nullable=True)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
