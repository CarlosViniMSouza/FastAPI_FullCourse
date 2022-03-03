from pydantic import BaseModel


class BlogVars(BaseModel):
    title: str
    body: str


class ShowBlog(BlogVars):
    title: str
    body: str

    class Config():
        orm_mode = True


class User(BaseModel):
    name: str
    email: str
    pwd: str
