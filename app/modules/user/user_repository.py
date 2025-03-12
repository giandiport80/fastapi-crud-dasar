from sqlalchemy.orm import Session
from app.modules.user.user_model import User
from sqlalchemy import select

def get_users(db: Session):
    return db.query(User).all()
    # return db.execute(select(User.id, User.name)).mappings().all()


def find_by_id(id: int, db: Session):
    return db.query(User).filter(User.id == id).first()