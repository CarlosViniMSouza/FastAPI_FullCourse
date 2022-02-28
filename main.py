from fastapi import FastAPI

app = FastAPI()


@app.get("/blogs")
async def index():
    return {"data": "Blogs list"}


@app.get("/blog/unpublished")
async def unpublished():
    return {"data": "blogs unpublished"}


@app.get("/blog/{id}")
async def show(id: int):
    # fecth blog with id = {id}
    return {"data": f"Blog N° {id}"}


@app.get("/blog/{id}/comments")
async def comments(id: int):
    return {"data": "A Great Blog! Recommended"}


# For access the documentation:
# http://127.0.0.1:8000/docs (Swagger UI)
# http://127.0.0.1:8000/redoc (Redoc UI)
