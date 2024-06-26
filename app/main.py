from fastapi import FastAPI
import psycopg2
from . import models
from .database import engine
from .routers import user,post
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI() 

origins=['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# models.Base.metadata.create_all(bind=engine)

app.include_router(post.router)
app.include_router(user.router)

@app.get('/') 
def read_root(): 
  return 'Home' 

