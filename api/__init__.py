from fastapi import APIRouter
import model
from typing import Union
from data import Data

api_root = APIRouter()


@api_root.get("/book", response_model=Union[model.Response200, model.Response404])
async def book_description(book_id: str):
    response = Data.book(book_id)
    if response is not None:
        book_info = model.BookInfo(
            book_id=book_id,
            book_name=response.xpath(model.BookXpath.book_name)[0],
            author_name=response.xpath(model.BookXpath.author_name)[0],
            update_time=response.xpath(model.BookXpath.update_time)[0],
            update_chapter=response.xpath(model.BookXpath.update_chapter)[0],
            description=response.xpath(model.BookXpath.description)[0].replace(" ", ""),
            book_state=response.xpath(model.BookXpath.book_state)[0],
            cover_url="https://www.qu-la.com" + response.xpath(model.BookXpath.cover_url)[0],
            catalogue=[
                {"chapter_url": i.attrib['href'], "chapter_name": i.text} for i in
                response.xpath(model.BookXpath.catalogue)
            ]
        )
        return model.Response200(data=book_info.dict())
    return model.Response404(message="get book info failed, book_id is {}".format(book_id))


@api_root.get("/search", response_model=Union[model.Response200, model.Response404])
async def search_api(q: str):
    response = Data.search(q)
    if response is not None:
        search_result = []
        for i in response.xpath(model.BookXpath.search_result):
            search_result.append({
                'book_name': i.text,
                'book_url': i.attrib['href'].replace('http://www.qu-la.com/book/goto/id/', ''),
            })
        return model.Response200(data=model.Search(search_result=search_result).dict())
    return model.Response404(message="search failed, keyword is {}".format(q))


@api_root.get("/chapter", response_model=Union[model.Response200, model.Response404])
async def content_api(book_id: Union[str, int], chapter_id: Union[str, int]):
    response = Data.chapter(book_id, chapter_id)
    if response is not None:
        chapter_info = model.Chapter(
            chapter_title=response.xpath(model.BookXpath.chapter_title)[0].strip(),
            content='\n'.join(response.xpath(model.BookXpath.content)).replace('\r', '\n')
        )
        return model.Response200(data=chapter_info.dict())
    return model.Response404(message="get chapter info failed, chapter_id is {}".format(chapter_id))
