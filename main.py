
""" NUESTRO PRIMER API - PROYECTO CLON DE TWITTER - FASTAPI - PYTHON"""

# Python
from datetime import date
from datetime import datetime
from tkinter import N
from typing import Optional
from uuid import UUID

# Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field

# FastAPI
from fastapi import FastAPI

app = FastAPI()

# Models

class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)

class UserLogin(UserBase):
    passwrod: str = Field(
        ...,
        min_length=8,
        max_length=24
        )

class User(UserBase):
    first_name: str = Field(
        ...,
        min_length=4,
        max_length=50
    )
    last_name: str = Field(
        ...,
        min_length=4,
        max_length=50
    )
    birth_date: Optional[date] = Field(default=None) 

class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(
        ...,
        min_length=1,
        max_length=256
        )
    create_at: datetime = Field(default=datetime.today())
    update_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)



@app.get(path="/")
def home():
    return {"Twitter API": "Working!"}