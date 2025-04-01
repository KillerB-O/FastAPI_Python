from blog import database
from sqlalchemy import Column,Integer,String

class Blog(database.Base):
    __tablename__="blogs"

    ID=Column(Integer,primary_key=True,index=True)
    title=Column(String)
    body=Column(String)

class User(database.Base):
    __tablename__="User_info"

    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String)
    Email=Column(String,unique=True,nullable=False)
    password=Column(String)