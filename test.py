import requests
import json


def get_book_description(book_id):
    result = requests.get(url="http://127.0.0.1:8000/book?book_id={}".format(book_id))
    result.encoding = 'utf-8'
    for i in range(10):
        if result.status_code == 200:
            print(json.loads(result.text))
            # return json.loads(result.text)
        else:
            print(result.status_code)


get_book_description("2_2219")
