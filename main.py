from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/role")
def role():
    name, job, time = "Carlos", "Software Developer", 2
    return {
        "name": f"{name}",
        "job": f"{job}",
        "time": f"{time} years"
    }


@app.get("/blogs")
async def index():
    return {"data": "Blogs list"}


@app.get("/blog/unpublished")
async def unpublished():
    return {"data": "blogs unpublished"}


@app.get("/blog/{id}")
async def index(id: int):
    # fecth blog with id = {id}
    return {"data": f"Blog N° {id}"}


@app.get("/blog/{id}/comments")
async def comments(id: int):
    return {"data": "A Great Blog! Recommended"}
