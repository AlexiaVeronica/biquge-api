import src
from fastapi import APIRouter
import model

book_info_api = APIRouter()


@book_info_api.get("/book", response_model=model.Response200)
def book_description(book_id: str):
    response = src.request(url="https://www.qu-la.com/booktxt/{}".format(book_id))
    if not isinstance(response, int):

        # BookInfo.book_id = book_id
        # BookInfo.book_name = response.xpath(src.rule.Book.book_name)[0]
        # BookInfo.author_name = response.xpath(src.rule.Book.author_name)[0]
        # BookInfo.update_time = response.xpath(src.rule.Book.update_time)[0]
        # BookInfo.update_chapter = response.xpath(src.rule.Book.update_chapter)[0]
        # BookInfo.description = response.xpath(src.rule.Book.description)[0].replace(" ", "")
        # BookInfo.book_state = response.xpath(src.rule.Book.book_state)[0]
        # BookInfo.cover_url = "https://www.qu-la.com" + response.xpath(src.rule.Book.cover_url)[0]
        # BookInfo.catalogue = [
        #     {"chapter_url": i.attrib['href'], "chapter_name": i.text} for i in response.xpath(src.rule.Book.catalogue)
        # ]
        BookInfo = model.BookInfo(
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
        return model.Response200(data=BookInfo.dict())



    else:
        return {"code": response, "message": "get book info failed, book_id is {}".format(book_id)}
