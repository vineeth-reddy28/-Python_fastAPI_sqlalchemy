from typing import Optional, List
from fastapi import FastAPI
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from .import models, schemas, utils
from .database import engine, SessionLocal
from .routers import post, user, auth, vote
from fastapi.middleware.cors import CORSMiddleware
from .config import settings


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# my_posts = [{"title": "title pf post 1", "content": "content of post 1", "id": 1},
#             {"title": "favourite food", "content": "I like pizza", "id": 2}]

# def find_post(id):
#     for p in my_posts:
#         if p['id'] == id:
#             return p


# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p['id'] == id:
#             return i


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Hello World"}
