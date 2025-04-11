from fastapi import FastAPI
from blog import model
from.database import engine
from .routers import blog,user,authentication

model.database.Base.metadata.create_all(bind=engine)       #importing All database model from model package


app=FastAPI()

app.include_router(authentication.router)
app.include_router(blog.router)                         #routes the control to the specific module of routers directory
app.include_router(user.router)
