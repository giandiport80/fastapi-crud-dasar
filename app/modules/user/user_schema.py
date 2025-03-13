from pydantic import BaseModel, EmailStr, Field, field_validator
import re


class UserRequest(BaseModel):
    name: str = Field(..., min_length=3)
    email: EmailStr
    password: str = Field(..., min_length=6)

    @field_validator("name")
    @classmethod
    def validate_no_html(cls, value):
        """Pastikan field tidak mengandung tag HTML"""
        if re.search(r"<[^>]*>", value):
            raise ValueError("Tidak boleh mengandung tag HTML")
        return value
