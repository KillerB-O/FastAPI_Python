from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app=FastAPI()

@app.get("/")
def Home():
    return {'data':{'content':"Hello People!,Welcome to my website!"}}

@app.get('/blog')
def show(limit=10,published=True,sort:Optional[str]=None):
    if published:
        return{'data':f"{limit} published blogs from the db"}
    else:
        return{'data':f"{limit} unpublished blogs from the db"}

@app.get('/blog/{id}/comments')
def show_comments(id):
    return {'data':{'1':"wow!,I have never seen such a wonderful Blog!!!!",'2':"FR!,even i have never seen such a thing in my life before.This is truly eye opening  T---T."}}

@app.get('/blog/{id}')
def blog(id:int):
    return {'data':{id}}

class Blog(BaseModel):
    title:str
    body:str
    publish:Optional[bool]
@app.post('/blog')
def create_blog(blog:Blog):
           return{'data':f"A blog of title {blog.title} has been created.",'body':f"{blog.body}"}




if __name__=='__main__':
     uvicorn.run(app,host='127.0.0.1',port=9000)