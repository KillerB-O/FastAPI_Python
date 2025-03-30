from fastapi import FastAPI

app=FastAPI()

@app.get('/')
def index():
    return{'data':"blog list"}

@app.get('/about')
def about():
    #fetch blog with id=id
    return{'data':'About Website,Just trying the new webframework!!'}

@app.get('/blog/{id}')
def show(id):
    #fetch blog with id=id
    return{'data':id}
