
import requests
import json


def test_book_description(book_id):
    result = requests.get(url="http://127.0.0.1:8000/api/book?book_id={}".format(book_id))
    result.encoding = 'utf-8'
    if result.status_code == 200:
        print(json.loads(result.text))
        # return json.loads(result.text)
    else:
        print(result.status_code)


test_book_description("29218062116")
