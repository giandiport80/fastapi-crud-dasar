from pydantic import BaseModel, EmailStr, Field, field_validator

from app.handlers.handler import validate_no_html


class UserRequest(BaseModel):
    name: str = Field(..., min_length=3)
    email: EmailStr
    password: str = Field(..., min_length=6)

    _validate_no_html = field_validator("name", "email")(validate_no_html)


class UserUpdateRequest(BaseModel):
    name: str = Field(..., min_length=3)
    email: EmailStr

    _validate_no_html = field_validator("name", "email")(validate_no_html)