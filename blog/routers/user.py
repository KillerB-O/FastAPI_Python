from fastapi import APIRouter,Depends,status,Response
from sqlalchemy.orm import Session
from..import schema,model,database
from..database import get_db
from..encryption import Hash
from blog.repository import user

router=APIRouter(
   prefix="/user",
   tags=["Users"])


@router.post('/',status_code=status.HTTP_201_CREATED)
def create_user(request:schema.User,db:Session=Depends(get_db)):
   return user.create(request,db)

@router.get('/',response_model=list[schema.Showuser],status_code=status.HTTP_200_OK)
def display_user(response:Response,db:Session=Depends(get_db)):
    return user.get_all(db)

@router.get('/{id}',response_model=schema.Showuser,status_code=status.HTTP_200_OK)
def display_user(id,response:Response,db:Session=Depends(get_db)):
  return user.get_id(id,db)