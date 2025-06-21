from fastapi import FastAPI
from app.api import router

app = FastAPI(title="Student Tutor Chatbot")

app.include_router(router) 