from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "Python Basics",
        "author": "Guido",
        "publish_date": "2023"
    },
    {
        "id": 2,
        "title": "FastAPI",
        "author": "Sebastian",
        "publish_date": "2024"
    }
]


class Book(BaseModel):
    id: int
    title: str
    author: str
    publish_date: str
