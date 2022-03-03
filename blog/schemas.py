from pydantic import BaseModel


class BlogVars(BaseModel):
    title: str
    body: str


class ShowBlog(BlogVars):
    class Config():
        orm_mode = True
