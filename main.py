from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get("/blog/unpublished")
async def unpublished():
    return {"data": "blogs unpublished"}


# Here we are playing with the parameters of the functions

@app.get("/blog/{id}/comments")
async def comments(id: int):
    return {"data": "A Great Blog! Recommended"}


@app.get("/blog/{id}")
async def show(id: int, limit: int):
    # fecth blog with id = {id}
    return {"data": f"Blog N° {id}"}


@app.get("/blog")
async def index(limit: int, published: bool, sort: Optional[str] = None):
    if published:
        return {"data": f"{limit} published on DB"}
    else:
        return {"data": f"{limit} unpublished on DB"}


# here we are testing functions of Method POST() + class Python

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post("/blog")
async def createBlog(req: Blog):
    return {"msg": f"This blog contain: One {req.title}, One {req.body} and a optional status call {req.published}"}


# For access the documentation:
# http://127.0.0.1:8000/docs (Swagger UI)
# http://127.0.0.1:8000/redoc (Redoc UI)
