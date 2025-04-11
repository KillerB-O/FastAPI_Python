from pydantic import BaseModel


class Blog(BaseModel):       #Base Request schema
    title:str
    body:str


class User(BaseModel):
    name:str
    Email:str
    password:str

class Showuser(BaseModel):
    name:str
    Email:str
    class Config():
        orm_model=True

class ShowBlog(BaseModel):        #Responce Schema[schema is for request model]
    title:str
    body:str
    creator:Showuser
    
    class Config():
        orm_mode=True

class login(BaseModel):
    username:str
    password:str        