from pydantic import BaseModel
from typing import Optional, List


class BookInfo(BaseModel):
    book_id: str
    book_name: str
    author_name: str
    update_time: str
    update_chapter: str
    description: str
    book_state: str
    cover_url: str
    catalogue: list


class Chapter(BaseModel):
    chapter_title: str
    content: str


class Search(BaseModel):
    search_result: list[dict[str, str]]


class ChapterParams(BaseModel):
    book_id: int = 0
    chapter_id: int = 0


class Response200(BaseModel):
    code: int = 200
    message: str = "success"
    data: dict = {}


class Response404(BaseModel):
    code: int = 404
    message: str = "not found"
    data: Optional[dict] = None


class Response500(BaseModel):
    code: int = 500
    message: str = "server error"
    data: Optional[dict] = None


class Token(BaseModel):
    access_token: str
    token_type: str
