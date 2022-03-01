from pydantic import BaseModel


class BlogVars(BaseModel):
    title: str
    body: str
