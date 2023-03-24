from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)

print(get_password_hash("a"))

print(get_password_hash("a"))


hashed_password = "$2b$12$ExjcKl0QP6vlD3lBMf9Btu1.4pKpVlRwzIc/0JdL8wgP5teHaTv6y"
hashed_passwordb = "$2b$12$jjFXMoJhykV11GCvviAjleXK7a.HMyVAQIE4FGdVa6n2L8Onl9gVS"

print (verify_password("a", hashed_passwordb))

# @app.get("/users/me/items/")
# async def read_own_items(current_user: User = Depends(get_current_active_user)):
#     content = [{"item_id": "Foo", "owner": current_user.username}]
#     response = JSONResponse(content=content)
   
#     refreshed_token = refresh_token(current_user)
#     response.set_cookie(key= "Authorization", value = "Bearer " + refreshed_token )
    
#     return response
