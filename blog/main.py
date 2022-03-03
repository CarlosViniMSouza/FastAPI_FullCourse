from fastapi import FastAPI, Depends, Response, HTTPException, status
from db import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List, Dict
import models, schemas, hashing
import uvicorn

app = FastAPI()

models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def hello():
    return {"message": "hello"}


@app.get("blog/all", response_model=List[schemas.ShowBlog])
async def allBlogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()

    return blogs


@app.get("blog/{id}", status_code=200, response_model=schemas.ShowBlog)
async def specificBlog(id, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog of id: {id} -> Not Available"
        )

    return blog


@app.post("/blog", status_code=status.HTTP_201_CREATED)
async def createBlog(req: schemas.BlogVars, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=req.title, body=req.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog


@app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def deleteBlog(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog of id: {id} -> Not Available"
        )

    blog.delete(synchronize_session=False)
    db.commit()

    return 'Blog deleted'


@app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED)
async def updateBlog(id, req: schemas.BlogVars, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog of id: {id} -> Not Available"
        )

    blog.update(req)
    db.commit()

    return 'Updated blog'


@app.get("/user", response_model=schemas.ShowUser)
async def getUser(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User of id: {id} -> Not Available"
        )

    return user


@app.post("/user", response_model=schemas.ShowUser)
async def createUser(req: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(name=req.name, email=req.email,
                           pwd=hashing.Hash.bcrypt(req.pwd))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
# continue in 1:38:53
