from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get("/blog/unpublished")
async def unpublished():
    return {"data": "blogs unpublished"}


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

# For access the documentation:
# http://127.0.0.1:8000/docs (Swagger UI)
# http://127.0.0.1:8000/redoc (Redoc UI)
