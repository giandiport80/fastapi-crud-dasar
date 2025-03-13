from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from app.config.database import get_db
from app.modules.user import user_repository
from app.modules.user.user_schema import UserRequest

router = APIRouter()

@router.get("/users", tags=["Users"], status_code=200)
def get_index_users(db: Session = Depends(get_db)):
    data = user_repository.get_users(db)

    return {
        "success": True,
        "data": data
    }


@router.get("/users/{id}", tags=["Users"], status_code=200)
def find_by_id(id: int, db: Session = Depends(get_db)):
    data = user_repository.find_by_id(id, db)

    if not data:
        return JSONResponse(
            status_code=404,
            content={
                "success": False,
                "message": "data tidak ditemukan"
            }
        )

    return {
        "success": True,
        "data": data
    }


@router.post("/users", status_code=201)
def store(user: UserRequest, db: Session = Depends(get_db)):
    new_user = user_repository.create(user, db)

    return {
        "success": True,
        "message": "Data berhasil disimpan",
        "data": new_user
    }
