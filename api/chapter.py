import src
from fastapi import APIRouter
import model

chapter_info_api = APIRouter()


@chapter_info_api.get("/chapter", response_model=model.Response200)
def content_api(book_id, chapter_id: str):
    response = src.request(url="https://www.qu-la.com/booktxt/{}/{}.html".format(book_id, chapter_id))
    if not isinstance(response, int):  # 判断是否是int类型，如果是int类型，说明请求失败
        chapter_info = model.Chapter(
            chapter_title=response.xpath(src.rule.Chapter.chapter_title)[0].strip(),
            content='\n'.join(response.xpath(src.rule.Chapter.content)).replace('\r', '\n')
        )
        return model.Response200(data=chapter_info.dict())
    else:
        return {"code": response, "message": "get chapter info failed, book_id is {}".format(book_id)}
