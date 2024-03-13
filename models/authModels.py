from pydantic import BaseModel, EmailStr


class SignUpModel(BaseModel):
    email: EmailStr
    password: str

    # class Config:
    #     schema_extra = {
    #         "example": {"email": "sample@gmail.com", "password": "password123@"}
    #     }


class LoginModel(BaseModel):
    email: EmailStr
    password: str

    # class config:
    #     schema_extra = {
    #         "example": {"email": "sample@gmail.com", "password": "password123@"}
    #     }
