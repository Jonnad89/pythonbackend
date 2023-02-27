from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()
# uvicorn users:app --reload
# Entidad user
class User(BaseModel):
    id: int
    name: str
    surname:str
    url: str
    age: int

users_list = [User(id=1, name ="Jonatan", surname="Di vincenzo", url="http://instagram.com/jonnad89", age= 33 ),
User(id=2,name ="liliana", surname="Nenna", url="http://instagram.com/liliananenna", age= 70 ),
User(id=3, name ="Humi", surname="Di vincenzo", url="http://instagram.com/humito", age= 2)]


@router.get("/users")
async def users():
    return users_list
      # http://127.0.0.1:8000/users
#path
@router.get("/user/{id}")
async def user(id: int):
  return search_user(id)
#Query 
@router.get("/user/")
async def user(id: int):
   return search_user(id)

@router.post("/user/",response_model=User, status_code=201)
async def user(user: User):
  if type(search_user(user.id)) == User:
    raise HTTPException(status_code=404,detail="El usuario ya existe")
  else:  
    users_list.append(user)
    return user 

@router.put("/user/")
async def user(user: User):
   
   found = False

   for index,saved_user in enumerate(users_list):
      if saved_user.id == user.id: 
         users_list[index] = user
         found = True
   if not found:
       return {"error": "No se ha actualizado el usuario"} 
   else:
      return user    
             

def search_user(id:int):
    users = filter(lambda user: user.id == id, users_list)
    try:
      return list(users)[0]
    except:
      return {"error": "No se ha encontrado el usuario"}

@router.delete("/user/{id}")
async def user(id: int):
   
   found = False

   for index,saved_user in enumerate(users_list):
      if saved_user.id == id: 
         del users_list[index]
         found = True
   if not found:
          return {"error": "No se ha eliminado el usuario"}   
   else: 
      return {"El usuario se ha elminado correctamente"}   

















"""
@app.get("/usersjson")
async def usersjson(): 
    return [{"name":"Jonatan", "surname" :"Di vincenzo", "url":"http://instagram.com/jonnad89", "age":33},
            {"name":"liliana", "surname" :"Nenna", "url":"http://instagram.com/lilianannena", "age": 70},
             {"name":"Humi", "surname" :"Di vincenzo", "url":"http://instagram.com/Humito", "age":2}, ] 
"""
