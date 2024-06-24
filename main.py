from fastapi import FastAPI
from routers import books, authors
from database import init_db

app = FastAPI()

init_db()

app.include_router(books.router, prefix="/books", tags=["books"])
app.include_router(authors.router, prefix="/authors", tags=["authors"])