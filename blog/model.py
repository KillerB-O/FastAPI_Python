from blog import database
from sqlalchemy import Column,Integer,String

class Blog(database.Base):
    __tablename__="blogs"
    ID=Column(Integer,primary_key=True,index=True)
    title=Column(String)
    body=Column(String)