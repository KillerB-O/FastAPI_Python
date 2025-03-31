from pydantic import BaseModel


class Blog(BaseModel):       #Base Request schema
    title:str
    body:str

class ShowBlog(Blog):        #Responce Schema[schema is for request model]
    class Config():
        orm_mode=True