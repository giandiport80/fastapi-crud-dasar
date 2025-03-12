from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing_extensions import Generic, Optional, TypeVar, List

DATABASE_URL = "mysql+pymysql://root@localhost:3306/app_fastapi_crud_dasar"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


T = TypeVar("T")

class BaseResponse(BaseModel, Generic[T]):
    success: bool = None
    message: Optional[str] = None
    data: Optional[T] = None
    error: Optional[str] = None
    errors: Optional[List[str]] = None

    class Config:
        json_encoders = {None: lambda v: None}  # ✅ Mencegah `None` muncul di JSON

    def model_dump(self, **kwargs):
        """Override agar otomatis exclude_none=True"""
        kwargs.setdefault("exclude_none", True)  # ✅ Otomatis hilangkan `None`
        return super().model_dump(**kwargs)