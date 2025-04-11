from..import model
from sqlalchemy.orm import Session
from fastapi import status,HTTPException
from..encryption import Hash

def get_all(db:Session):
    new_user=db.query(model.User).all()
    return new_user

def get_id(id,db:Session):
    User_data=db.query(model.User).filter(model.User.id==id).first()
    return User_data

def create(request,db:Session):
    new_user=model.User(name=request.name,Email=request.Email,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
