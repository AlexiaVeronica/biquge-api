from fastapi import APIRouter
import src
import model
from typing import Union

search_info_api = APIRouter()


@search_info_api.get("/search", response_model=Union[model.Response200, model.Response404])
def search_api(q: str):
    params = {"ie": "utf-8", "siteid": "qu-la.com", "q": q}
    response = src.request(url="https://so.biqusoso.com/s1.php", params=params, encoding='utf-8')
    if response is not None:
        search_result = []
        for i in response.xpath(src.rule.Search.search_result):
            search_result.append({
                'book_name': i.text,
                'book_url': i.attrib['href'].replace('http://www.qu-la.com/book/goto/id/', ''),
            })
        return model.Response200(data=model.Search(search_result=search_result).dict())
    return model.Response404(message="search failed, keyword is {}".format(q))
