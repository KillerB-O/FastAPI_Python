from..import model
from sqlalchemy.orm import Session
from fastapi import status,HTTPException

def Show_all(db:Session):
    blogs= db.query(model.Blog).all()
    return blogs

def create(request,db:Session):
    new_blog=model.Blog(title=request.title,body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id,db:Session):
    db.query(model.Blog).filter(model.Blog.ID==id).delete(synchronize_session=False)
    db.commit() 
    return 'Done!'      

def update(id:int,db:Session,request):
    db.query(model.Blog).filter(model.Blog.ID==id).update(request.dict())
    db.commit()                                                               #updates the Blog of id=id from database
    return 'updated'

def Show_Id(id,db:Session):
    blog=db.query(model.Blog).filter(model.Blog.ID==id).first()               
    if not blog:                                                      #Shows The Blog of id=id Stored in the database
   
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with the ID {id} is not available")
       
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {'detail':f"Blog with the ID {id} is not available"}
    
    return blog
