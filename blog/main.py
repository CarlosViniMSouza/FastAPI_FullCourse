from fastapi import FastAPI
from db import engine
import models, schemas
import uvicorn

app = FastAPI()

models.Base.metadata.create_all(engine)


@app.get("/blog/entry")
async def creatingBlogs():
    return {"message": "Blog in construction..."}


@app.post("/blog")
async def createBlog(req: schemas.BlogVars):
    return req


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
