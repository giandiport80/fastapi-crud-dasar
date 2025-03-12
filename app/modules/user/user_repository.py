from sqlalchemy.orm import Session
from app.modules.user.user_model import User

def get_users(db: Session):
    return db.query(User).all()