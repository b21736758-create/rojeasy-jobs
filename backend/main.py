from fastapi import FastAPI
from database import engine
import models  # 👈 VERY IMPORTANT

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
