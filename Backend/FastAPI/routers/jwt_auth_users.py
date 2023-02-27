from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1
# acceder a la libreria openssl rand -hex 32      para generar el secret
SECRET ="9138d1034defe2357139fda7442aaf5a669fe3381ebe3fedb1c739a40cf94f4d"


router = APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl="login") #endpoint
#instalar:
#  pip install "python-jose[cryptography]"    luego de instalar esto, lo importamos "from jose import jwt"
# pip install "passlib[bcrypt]"

crypt = CryptContext(schemes=["bcrypt"])

class User(BaseModel):
    username: str
    full_name:str
    email: str
    disabled: bool

class UserDB(User): #heredo User
    password: str

users_db = {
    "jonatan": {
         "username": "jonatan",
         "full_name":"Jonatan Di Vincenzo",
         "email": "jonnadvwork@gmail.com",
         "disabled": False,
         "password" : "$2a$12$ok8qNxY04OVZZEiwvD4MS.sSVylMdzjLeUSTrrf1YG.PpE0kOAOUS"
    },
    "jonatan2": {
         "username": "Jonatan2",
         "full_name":"Jonatan Di Vincenzo2",
         "email": "jonnadvwork2@gmail.com",
         "disabled": True,
         "password" : " $2a$12$pR08qO5cOkL07Ufhi7DuR.mFQtGf.kJAIfGELUV/6T5reRWxThLCG "
    }
}
def search_user_db(username: str): 
    if username in users_db:
        return UserDB(**users_db[username])
    
def search_user(username: str): 
    if username in users_db:
        return User(**users_db[username])    


async def auth_user(token:str = Depends(oauth2)):
    
    exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales de autenticación inválidas", 
            headers={"www-Authenticate":"Bearer"})

    try:

      username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
      if username is None:
            raise exception

    except JWTError:
          raise exception
    
    return search_user(username)
    
async def current_user(user: User = Depends(auth_user)):
    if user.disabled:
         raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario inactivo")
        
    return user    


@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
      raise HTTPException(status_code=400,detail="El usuario no es correcto")

    user = search_user_db(form.username)

    if not crypt.verify(form.password, user.password):
        raise HTTPException(status_code=400,detail="La constraseña no es correcta")

    expire = datetime.utcnow() +  timedelta(minutes=ACCESS_TOKEN_DURATION)

    access_token = {
        "sub": user.username, 
        "exp": expire
    }
  
    return {"access_token": jwt.encode(access_token,SECRET, algorithm=ALGORITHM), "token_type":"bearer"}

@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user