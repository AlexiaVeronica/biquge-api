import fastapi
import uvicorn
from starlette.middleware.cors import CORSMiddleware
from api import book, chapter, search

app = fastapi.FastAPI()

app.include_router(book.book_info_api, prefix="/api")

app.include_router(search.search_info_api, prefix="/api")

app.include_router(chapter.chapter_info_api, prefix="/api")


@app.get("/")
def read_root():
    return {"Hello": "Hello World"}


if __name__ == '__main__':
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # 设置允许访问的域名,"*"，即为所有,允许的origins来源
        allow_credentials=True,
        allow_methods=["*"],  # 设置允许跨域的http方法，比如 get、post、put等。
        allow_headers=["*"]
    )  # 允许跨域的headers，可以用来鉴别来源等作用。

    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True, debug=True)
