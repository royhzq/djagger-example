from pydantic import BaseModel as Schema, Field
from typing import List
import datetime


class ArticleRequestSchema(Schema):
    year: int
    month: int
    slug: str


class ArticleDetailSchema(Schema):
    created: datetime.datetime
    title: str
    author: str
    content: str


class ArticleCreateSchema(Schema):
    """POST schema for blog article creation"""

    title: str = Field(description="Title of Blog article")
    content: str = Field(description="Blog article content")


class ArticleDeleteSchema(Schema):
    pk: int = Field(description="Primary key of article to delete")


class ArticleYearSchema(Schema):
    year: int


class ArticlePageSchema(Schema):
    page: int


class ArticleHeaderSchema(Schema):
    api_key: str


class ArticleCookieSchema(Schema):
    username: str


class AuthorSchema(Schema):
    first_name: str
    last_name: str


class AuthorListSchema(Schema):
    authors: List[AuthorSchema]


class AuthorIdSchema(Schema):
    pk: int


class CategoryListSchema(Schema):
    """List of category names"""

    name: List[str]
