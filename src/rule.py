class WebRule:
    def __init__(self, url, method, callback):
        self.url = url
        self.method = method
        self.callback = callback

    def match(self, url, method):
        return (self.url == url) and (self.method == method)

    def __call__(self, *args, **kwargs):
        return self.callback(*args, **kwargs)


class Book:
    book_name = '//*[@id="list"]/div[1]/div[2]/h1/text()'
    author_name = '//*[@id="list"]/div[1]/div[2]/span/text()'
    update_time = '//*[@id="list"]/div[2]/p[2]/span/text()'
    update_chapter = '//*[@id="list"]/div[2]/p[2]/a/text()'
    description = '//*[@id="list"]/div[1]/div[2]/div[2]/text()'
    book_state = '//*[@id="list"]/div[1]/div[2]/div[1]/span[2]/text()'
    catalogue = '//*[@id="list"]/div[3]/ul[2]/li/a'
    cover_url = '//*[@id="fengmian"]/a/img/@src'


class Search:
    search_result = '//*[@id="search-main"]/div[1]/ul/li/span/a'


class Chapter:
    chapter_title = '//*[@id="chapter-title"]/h1/text()'
    content = '//*[@id="txt"]/text()'
