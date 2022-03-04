from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from blog import models, schemas, db
from typing import List


router = APIRouter()

get_db = db.get_db


@router.get("blog/all", response_model=List[schemas.ShowBlog], tags=['Blogs'])
async def allBlogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()

    return blogs


@router.post("/blog", status_code=status.HTTP_201_CREATED, tags=['Blogs'])
async def createBlog(db: Session = Depends(get_db)):
    new_blog = models.Blog(title=req.title, body=req.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog


@router.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=['Blogs'])
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


@router.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED, tags=['Blogs'])
async def updateBlog(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog of id: {id} -> Not Available"
        )

    blog.update(req)
    db.commit()

    return 'Updated blog'
