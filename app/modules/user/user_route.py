from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from typing_extensions import List

from app.config.database import get_db, BaseResponse
from app.modules.user import user_repository
from app.modules.user.user_schema import UserResponse

router = APIRouter()

@router.get(
    "/users",
    tags=["Users"],
    status_code=200,
    response_model=BaseResponse[List[UserResponse]],
    response_model_exclude_none=True
)
def get_index_users(db: Session = Depends(get_db)):
    data = user_repository.get_users(db)

    response_data = [UserResponse.model_validate(user) for user in data]

    return BaseResponse(success=True, data=response_data)
