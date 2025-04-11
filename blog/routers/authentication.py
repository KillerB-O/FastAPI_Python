from sqlalchemy.orm import Session
from .. import schema,model,database
from fastapi import APIRouter,Depends,HTTPException,status
from..encryption import Hash
router=APIRouter(
    tags=['Authentication']
    )

@router.post('/login')
def login(request:schema.login,db:Session=Depends(database.get_db)):
    user=db.query(model.User).filter(model.User.Email==request.username).first()
    if not user :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invalid credentials")
    if not Hash.verify(request.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Incorrect password")

    #generate a JWT and return.    
    return "login"
