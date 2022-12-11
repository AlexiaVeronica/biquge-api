from fastapi import APIRouter
import src
import model

search_info_api = APIRouter()


@search_info_api.get("/search", response_model=model.Response200)
def search_api(q: str):
    params = {"ie": "utf-8", "siteid": "qu-la.com", "q": q}
    response = src.request(url="https://so.biqusoso.com/s1.php", params=params, encoding='utf-8')
    if not isinstance(response, int):
        search_result = []
        for i in response.xpath(src.rule.Search.search_result):
            search_result.append({
                'book_name': i.text,
                'book_url': i.attrib['href'].replace('http://www.qu-la.com/book/goto/id/', ''),
            })
        return model.Response200(data=model.Search(search_result=search_result).dict())
    else:
        return {"code": response, "message": "no search result, keyword is {}".format(q)}
