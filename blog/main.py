from fastapi import FastAPI,Depends,status,Response,HTTPException
from blog import schema,model
from.database import engine,SessionLocal
from sqlalchemy.orm import Session


model.database.Base.metadata.create_all(bind=engine)       #importing the database engine 

app=FastAPI()

def get_db():
    db=SessionLocal()                              # Initializing the database engine 
    try:
        yield db
    finally:
        db.close()    



@app.post('/blog',status_code=status.HTTP_201_CREATED)
def create(request:schema.Blog,db:Session=Depends(get_db)):                  #Create new Values into the data base
    new_blog=model.Blog(title=request.title,body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog



@app.get('/blog',status_code=status.HTTP_200_OK,response_model=list[schema.ShowBlog])
def all(response:Response,db:Session=Depends(get_db)):                                
    blogs=db.query(model.Blog).all()                                 #Shows all The Blogs Stored in the database
    return blogs


@app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db:Session=Depends(get_db)):
    db.query(model.Blog).filter(model.Blog.ID==id).delete(synchronize_session=False)
    db.commit() 
    return 'Done!'                                                 #deletes the Blog of id=id from database


@app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id,request:schema.Blog,db:Session=Depends(get_db)):
    db.query(model.Blog).filter(model.Blog.ID==id).update(request.dict())
    db.commit()                                                               #updates the Blog of id=id from database
    return 'updated'


@app.get('/blog/{id}',response_model=schema.ShowBlog,status_code=status.HTTP_200_OK)
def show(id,response:Response,db:Session=Depends(get_db)):
    blog=db.query(model.Blog).filter(model.Blog.ID==id).first()               
    if not blog:                                                      #Shows The Blog of id=id Stored in the database
   
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with the ID {id} is not available")
       
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {'detail':f"Blog with the ID {id} is not available"}
    
    return blog   


