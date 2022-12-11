import requests
from src import rule
from lxml import etree

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit'}


def request(url, method="GET", params=None, encoding="GBK"):
    result = requests.request(method=method, url=url, params=params, headers=headers)
    result.encoding = encoding
    if result.status_code == 200:
        return etree.HTML(result.text)
    return None


# print(request("https://www.qu-la.com/booktxt/{}".format(48697379116)))


def search_api(book_name: str):
    params = {"ie": "utf-8", "siteid": "qu-la.com", "q": book_name}
    response = request(url="https://so.biqusoso.com/s1.php", params=params, encoding='utf-8')
    if not isinstance(response, int):
        try:
            print([[i.text, i.attrib['href']] for i in response.xpath('//*[@id="search-main"]/div[1]/ul/li/span/a')])
            return [[i.text, i.attrib['href']] for i in response.xpath('//*[@id="search-main"]/div[1]/ul/li/span/a')]
        except Exception as error:
            print("search_api error, url is {}".format(error))
            return []
