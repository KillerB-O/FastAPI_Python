from fastapi import APIRouter,Response,status,Depends,HTTPException
from..import schema,database,model
from sqlalchemy.orm import Session
from.. database import get_db
from blog.repository import blog

router =APIRouter(
    prefix="/blog",
     tags=["Blogs "] )
 
 
@router.get('/',status_code=status.HTTP_200_OK,response_model=list[schema.ShowBlog],)
def all(response:Response,db:Session=Depends(get_db)):                                
    return blog.Show_all(db)

@router.post('/',status_code=status.HTTP_201_CREATED,)
def create(request:schema.Blog,db:Session=Depends(get_db)):                  #Create new Values into the data base
    return blog.create(request,db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT,)
def destroy(id,db:Session=Depends(get_db)):
    return blog.destroy(id,db)                                           #deletes the Blog of id=id from database


@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED,)
def update(id,request:schema.Blog,db:Session=Depends(get_db)):
  return blog.update(id,db,request)

@router.get('/{id}',response_model=schema.ShowBlog,status_code=status.HTTP_200_OK,)
def show(id,response:Response,db:Session=Depends(get_db)):
    return blog.Show_Id