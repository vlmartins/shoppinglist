from pydantic import BaseModel
from fastapi.openapi.models import OAuth2


class Todo(BaseModel):
    desc: str


class User(BaseModel):
    username : str
    password: str
    roles : list | None = None
    accessToken : str | None = None
    refreshToken : str | None = None
    disabled: bool | None = False

class UserInDB(User):
    pwd: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class UserInDB(User):
    hashed_password: str



