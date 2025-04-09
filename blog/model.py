from blog import database
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship


class User(database.Base):
    __tablename__="User_info"

    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String)
    Email=Column(String,unique=True,nullable=False)
    password=Column(String)
    blogs=relationship('Blog',back_populates="creator")


class Blog(database.Base):
    __tablename__="blogs"

    ID=Column(Integer,primary_key=True,index=True)
    title=Column(String)
    body=Column(String)
    user_id=Column(Integer,ForeignKey('User_info.id'))
    creator=relationship('User',back_populates="blogs")

