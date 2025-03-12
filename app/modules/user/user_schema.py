from pydantic import BaseModel

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    password: str

    class Config:
        from_attributes = True
