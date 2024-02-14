from typing import Annotated
from datetime import datetime, timedelta, timezone

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from typing import Union

# openssl rand -hex 32. Secret key will used to sign the JWT tokens
SECRET_KEY = "6adc3de93310e0e03d1c7fb180eae06ecda93577b69c8760885b8f4ec44d3fb3"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$vM/9LTIl7W6HyJyzj7Nv0.SCJMFbhpGgwn8ii9AocASIdfyj.kY32",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": True,
    },
}

app = FastAPI()
"""
OAuth2 was designed so that the backend or API could be independent of server that autenticate he user
But FastAPI Application will handle the API and authenticatation. it is "password flow" that is one of many OAuth2 ways
1. Send username, password in Frontend
2. Check username, password and Response with token that will be expired after some time in API
3. Save temporarily token in Frontend and user is moved other section. Front end also need to fecth some more data from API
so that token will be used for authorization (Bearer <token>)
"""

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
# pwd context will used to hash and verify passwords
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    """
    oauth2_scheme is a Callable, so we can use Depends
    It is used in the OpenAPI Schema, using FastAPI's security schema
    FastAPI knows that oauth2_scheme is OAuth2PasswordBearer Class to define security schema

    This API is will check Heater Authorization if Bearer value is exist or not
    and return header value(token) as string and if it is not exist, it will be retuend as 401 status
    So, we don't need to check Header

    Args:
        token (Annotated[str, Depends): _description_

    Returns:
        _type_: _description_
    """
    return {"token": token}

class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    username: Union[str, None] = None
class User(BaseModel):
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None

class UserInDB(User):
    hashed_password: str
    
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)
    
def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)
    
def authenticate_user(fake_db, username:str, password:str ):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    # It is created for reponding new access token
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
    
    
def fake_hash_password(password: str):
    return "fakehashed" + password

def fake_decode_token(token):
    return User(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # Decode the received token, verify it
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        # If token is invalid, return an HTTP error, right away
        raise credentials_exception
    
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception

    # user = fake_decode_token(token)
    # if not user:
    #     raise HTTPException(
    #         status_code = status.HTTP_401_UNAUTHORIZED,
    #         detail="Invalid authentication credentials",
    #         headers={"WWW-Authenticate": "Bearer"}
    #     )
    return user

async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)]
):
    if current_user.disabled:
        raise HTTPException(stats_code=400, detail="Inactive")
    return current_user
    
@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    # user_dict = fake_users_db.get(form_data.username)
    # if not user_dict:
    #     raise HTTPException(status_code=400, detail="Incorrect username or password")
    # user = UserInDB(**user_dict)
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Athenticate": "Bearer"}
        )
    # hashed_password = fake_hash_password(form_data.password)
    # if not hashed_password == user.hashed_password:
    #     raise HTTPException(status=400, detail="Incorrect username or password")
    # return {"access_token": user.username, "token_type": "bearer"}
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # sub key should have a unique identifier across the entire application and should be a string
    # it is username in this example
    access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
    
    return Token(access_token=access_token, token_type="bearer")
    

@app.get("/users/me")
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", reload=True)
