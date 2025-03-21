from sqlalchemy.orm import Session

from app.helpers.helper import hashing_bcrypt, timestamp
from app.modules.user.user_model import User
from sqlalchemy import select

from app.modules.user.user_schema import UserRequest, UserUpdateRequest


def _field():
    return select(
        User.id,
        User.name,
        User.email,
        User.password,
        User.created_at,
        User.updated_at,
    ).select_from(User)


def get_users(db: Session):
    # return db.query(User).all()
    return db.execute(_field()).mappings().all()


def find_by_id(id: int, db: Session):
    return db.execute(_field().where(User.id == id)).mappings().first()


def create(user: UserRequest, db: Session):
    new_user = User(
        name=user.name,
        email=user.email,
        password=hashing_bcrypt(user.password),
        created_at=timestamp(),
        updated_at=timestamp(),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def cek_email_exist(email: str, db: Session) -> bool:
    return db.query(User).filter(User.email == email).first() is not None


def delete(id: int, db: Session):
    user = db.query(User).filter(User.id == id).first()

    if not user:
        return None

    db.delete(user)
    db.commit()

    return user


def update(id: int, user_data: UserUpdateRequest, db: Session):
    user = db.query(User).filter(User.id == id).first()

    if not user:
        return None

    user.name = user_data.name
    user.email = user_data.email
    user.updated_at = timestamp()

    db.commit()
    db.refresh(user)
    return user
