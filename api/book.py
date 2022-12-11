import src
from fastapi import APIRouter
import model
from typing import Union

book_info_api = APIRouter()


@book_info_api.get("/book", response_model=Union[model.Response200, model.Response404])
def book_description(book_id: str):
    response = src.request(url="https://www.qu-la.com/booktxt/{}".format(book_id))
    if response is not None:
        book_info = model.BookInfo(
            book_id=book_id,
            book_name=response.xpath(src.rule.Book.book_name)[0],
            author_name=response.xpath(src.rule.Book.author_name)[0],
            update_time=response.xpath(src.rule.Book.update_time)[0],
            update_chapter=response.xpath(src.rule.Book.update_chapter)[0],
            description=response.xpath(src.rule.Book.description)[0].replace(" ", ""),
            book_state=response.xpath(src.rule.Book.book_state)[0],
            cover_url="https://www.qu-la.com" + response.xpath(src.rule.Book.cover_url)[0],
            catalogue=[
                {"chapter_url": i.attrib['href'], "chapter_name": i.text} for i in
                response.xpath(src.rule.Book.catalogue)
            ]
        )
        return model.Response200(data=book_info.dict())
    return model.Response404(message="get book info failed, book_id is {}".format(book_id))
