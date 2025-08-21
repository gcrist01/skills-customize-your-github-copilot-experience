from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Example data model
class Book(BaseModel):
    id: int
    title: str
    author: str

books: List[Book] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Book API!"}

# Add CRUD endpoints here
# ...
