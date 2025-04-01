from pydantic import BaseModel


class Blog(BaseModel):       #Base Request schema
    title:str
    body:str

class ShowBlog(Blog):        #Responce Schema[schema is for request model]
    class Config():
        orm_mode=True

class User(BaseModel):
    name:str
    Email:str
    password:str

class Showuser(User):
    name:str
    Email:str
    class Config():
        orm_model=True