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
async def search_api(keyword: str):
    response = Data.search(keyword)
    if response is not None:
        search_result = []
        for index, data in enumerate(response.xpath(model.BookXpath.search_result), start=1):
            search_result.append({
                'index': index,
                'book_name': data.text,
                'book_url': data.attrib['href'].replace('booktxt', '').replace('/', ''),
            })
        return model.Response200(data=model.Search(search_result=search_result).dict())
    return model.Response404(message="search failed, keyword is {}".format(keyword))


@api_root.get("/chapter", response_model=Union[model.Response200, model.Response404])
async def content_api(book_id: Union[str, int] = 0, chapter_id: Union[str, int] = 0):
    if book_id == 0 or chapter_id == 0:
        return model.Response404(message="missing book_id or chapter_id")
    response = Data.chapter(book_id, chapter_id)
    if response is not None:
        chapter_info = model.Chapter(
            chapter_title=response.xpath(model.BookXpath.chapter_title)[0].strip(),
            content='\n'.join(response.xpath(model.BookXpath.content)).replace('\r', '\n')
        )
        return model.Response200(data=chapter_info.dict())
    return model.Response404(message="get chapter info failed, chapter_id is {}".format(chapter_id))


@api_root.get("/rank", response_model=Union[model.Response200, model.Response404])
async def rank_api(page: int, rank_type: model.Rank):
    rank_result = []
    if rank_type == model.Rank.day:
        response = Data.rank(page, model.Rank.day)
    elif rank_type == model.Rank.week:
        response = Data.rank(page, model.Rank.week)
    elif rank_type == model.Rank.month:
        response = Data.rank(page, model.Rank.month)
    elif rank_type == model.Rank.total:
        response = Data.rank(page, model.Rank.total)
    else:
        return model.Response404(message="rank_type error")

    if not response:
        return model.Response404(message="rank failed, page is {}".format(page))
    for index, data in enumerate(response.xpath(model.BookXpath.rank_result), start=1):
        rank_result.append({
            'index': index,
            'type': rank_type,
            'page': page,
            'book_name': data.text,
            'book_id': data.attrib['href'].replace('booktxt', '').replace('/', ''),
        })
    return model.Response200(data=model.Search(search_result=rank_result).dict())


@api_root.get("/class", response_model=Union[model.Response200, model.Response404])
async def class_api(page: int, class_type: model.BookClass):
    class_result = []
    if class_type == model.BookClass.xh:
        response = Data.book_class(page, model.BookClass.xh)
    elif class_type == model.BookClass.wy:
        response = Data.book_class(page, model.BookClass.wy)
    elif class_type == model.BookClass.cy:
        response = Data.book_class(page, model.BookClass.cy)
    elif class_type == model.BookClass.kh:
        response = Data.book_class(page, model.BookClass.kh)
    elif class_type == model.BookClass.finish:
        response = Data.book_class(page, model.BookClass.finish)
    elif class_type == model.BookClass.qt:
        response = Data.book_class(page, model.BookClass.qt)
    elif class_type == model.BookClass.ds:
        response = Data.book_class(page, model.BookClass.ds)
    elif class_type == model.BookClass.xj:
        response = Data.book_class(page, model.BookClass.xj)
    else:
        return model.Response404(message="class_type error")
    if not response is not None:
        return model.Response404(message="class failed, page is {}".format(page))
    for index, data in enumerate(response.xpath(model.BookXpath.class_result), start=1):
        class_result.append({
            'index': index,
            'type': class_type,
            'page': page,
            'book_name': data.text,
            'book_id': data.attrib['href'].replace('booktxt', '').replace('/', ''),
        })
    return model.Response200(data=model.Search(search_result=class_result).dict())
