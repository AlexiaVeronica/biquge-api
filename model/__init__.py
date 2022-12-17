from pydantic import BaseModel
from typing import Optional, List, Union
from enum import Enum


class BookInfo(BaseModel):
    book_id: str
    book_name: str
    author_name: Union[str, None]
    update_time: Union[str, None]
    update_chapter: Union[str, None]
    description: Union[str, None]
    book_state: Union[str, None]
    cover_url: Union[str, None]
    catalogue: List[dict]


class Chapter(BaseModel):
    chapter_title: str
    content: str


class Search(BaseModel):
    search_result: list[dict[str, str]]


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

class ResponseMissing(BaseModel):
    code: int = 400
    message: str = "missing params"
    data: Union[dict, list] = {}

class ResponseError(BaseModel):
    code: int = 500
    message: str = "server error"
    data: Union[dict, list] = {}


class Token(BaseModel):
    access_token: str
    token_type: str


class Rank(str, Enum):
    day = "dayvisit"
    week = "weekvisit"
    month = "monthvisit"
    total = "allvisit"


class BookClass(str, Enum):
    xh = "class1"
    xj = "class2"
    ds = "class3"
    cy = "class4"
    wy = "class5"
    kh = "class6"
    qt = "class7"
    finish = "finish"


class BookXpath:
    book_name: str = '//*[@id="list"]/div[1]/div[2]/h1/text()'
    author_name: str = '//*[@id="list"]/div[1]/div[2]/span/text()'
    update_time: str = '//*[@id="list"]/div[2]/p[2]/span/text()'
    update_chapter: str = '//*[@id="list"]/div[2]/p[2]/a/text()'
    description: str = '//*[@id="list"]/div[1]/div[2]/div[2]/text()'
    book_state: str = '//*[@id="list"]/div[1]/div[2]/div[1]/span[2]/text()'
    catalogue: str = '//*[@id="list"]/div[3]/ul[2]/li/a'
    cover_url: str = '//*[@id="fengmian"]/a/img/@src'
    search_result: str = '//*[@id="search-main"]/div[1]/ul/li/span/a'
    chapter_title: str = '//*[@id="chapter-title"]/h1/text()'
    content: str = '//*[@id="txt"]/text()'
    rank_result: str = '/html/body/div/div[2]/div[2]/div[1]/ul/li/div[3]/h4/a'
    class_result: str = '/html/body/div/div[2]/div[2]/div[1]/ul/li/div[2]/h4/a'
