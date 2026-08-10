from fastapi import FastAPI
from database import *
from router.router import router

Base.metadata.create_all(bind=engine)

app=FastAPI()

app.include_router(router)