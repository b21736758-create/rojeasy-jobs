from fastapi import FastAPI
from database import engine, Base
from models import User, Job
from sqlalchemy.orm import Session
from database import SessionLocal

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.post("/signup")
def signup(name: str, email: str, password: str, role: str):
    db = SessionLocal()
    user = User(name=name, email=email, password=password, role=role)
    db.add(user)
    db.commit()
    return {"msg": "signup success"}

@app.post("/jobs")
def post_job(title: str, location: str, skills: str):
    db = SessionLocal()
    job = Job(title=title, location=location, skills=skills)
    db.add(job)
    db.commit()
    return {"msg": "job posted"}

@app.get("/jobs")
def list_jobs():
    db = SessionLocal()
    return db.query(Job).all()
