import src
from fastapi import APIRouter
import model
from typing import Union

chapter_info_api = APIRouter()


@chapter_info_api.get("/chapter", response_model=Union[model.Response200, model.Response404])
def content_api(book_id, chapter_id: str):
    response = src.request(url="https://www.qu-la.com/booktxt/{}/{}.html".format(book_id, chapter_id))
    if response is not None:
        chapter_info = model.Chapter(
            chapter_title=response.xpath(src.rule.Chapter.chapter_title)[0].strip(),
            content='\n'.join(response.xpath(src.rule.Chapter.content)).replace('\r', '\n')
        )
        return model.Response200(data=chapter_info.dict())

    return model.Response404(message="get chapter info failed, chapter_id is {}".format(chapter_id))
