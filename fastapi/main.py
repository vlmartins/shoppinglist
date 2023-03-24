from datetime import datetime, timedelta
from fastapi import Depends, FastAPI, HTTPException, status, Request
from authcls import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from model import User, Token, TokenData, Todo
from database import (
    fetch_all_todos,
    create_todo,
    remove_todo,
    create_user,
    user_exists,
    db_fetch,
    db_fetch2,
)
from extra import user_regex
from crypt import verify_password, get_password_hash
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from secretkey import secret



SECRET_KEY = secret
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 9999



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://54.233.129.141",
    "http://54.233.129.141/",
    "http://localhost",
    "http://localhost/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def refresh_token(current_user):
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": current_user.username},
                                    expires_delta=access_token_expires)
    return access_token

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = await db_fetch2(token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: dict = Depends(get_current_user)):
    if current_user.disabled == True:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@app.post("/sign_up", response_model=None )
async def retrieve_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if user_regex(form_data) is False:
        raise HTTPException(418, "Invalid Username or Password")
    elif await user_exists(form_data):
        print("")
        form_data.password = get_password_hash(form_data.password)
        user = User(username = form_data.username, password= form_data.password)
        response = await create_user(user)
        if response:
            access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            access_token = create_access_token(data={"sub": form_data.username},
                                            expires_delta=access_token_expires)
            content = "User created"

            response = JSONResponse(content=content)

            response.set_cookie(key= "Authorization", value = "Bearer " + access_token)
            return response
    raise HTTPException(409, "Username Taken")


@app.post("/sign_in")
async def sign_in(form_data: OAuth2PasswordRequestForm = Depends()):
    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"},)

    db_user = await db_fetch(form_data)

    if db_user is False:
        raise exception
    elif not verify_password(form_data.password, db_user["password"]):
        raise exception

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": form_data.username},
                                    expires_delta=access_token_expires)
    content = {"access_token": "Success", "token_type": "bearer"}

    response = JSONResponse(content=content)
    response.set_cookie(key= "Authorization", value = "Bearer " + access_token)

    return response    


@app.get("/users/me/items/")
async def read_own_items(current_user: User = Depends(get_current_active_user)):
    content = await fetch_all_todos(current_user)
    response = JSONResponse(content=content)

    refreshed_token = refresh_token(current_user)
    response.set_cookie(key= "Authorization", value = "Bearer " + refreshed_token )
    
    return response

@app.post("/api/todo/", response_model=Todo)
async def post_todo(todo: Todo, current_user: User = Depends(get_current_active_user)):
    content = await create_todo(todo.dict(), current_user)
    if content:
        response = JSONResponse(content="Successfully created a todo!")

        refreshed_token = refresh_token(current_user)
        response.set_cookie(key= "Authorization", value = "Bearer " + refreshed_token )
        return response
    
    raise HTTPException(400, "Invalid")

@app.delete("/api/todo/{_id}")
async def delete_todo(_id, current_user: User = Depends(get_current_active_user)):

    content = await remove_todo(_id, current_user)
    if content:
        response = JSONResponse("Successfully deleted a todo")
        refreshed_token = refresh_token(current_user)
        response.set_cookie(key= "Authorization", value = "Bearer " + refreshed_token )
        return response
    raise HTTPException(404, f"There is no todo with the title {_id}")

@app.post('/register', response_model=User)
async def user_register(user: User) -> User:
    if user_regex(user) is False:
        raise HTTPException(418, "Invalid Username or Password")
    elif await user_exists(user):
        print("passou do user_exists")
        user.password = get_password_hash(user.password)
        response = await create_user(user.dict())
        if response:
            return dict(response)
    raise HTTPException(409, "Username Taken")