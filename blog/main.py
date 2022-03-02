from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db import engine, SessionLocal
import models, schemas
import uvicorn

app = FastAPI()

models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/blog/entry")
async def creatingBlogs():
    return {"message": "Blog in construction..."}


@app.get("blog/all")
def allBlogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@app.get("blog/{id}")
async def specificBlog(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    return blog


@app.post("/blog")
async def createBlog(req: schemas.BlogVars, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=req.title, body=req.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)

# continue in 1:38:53
