import time
from fastapi import FastAPI, Query
import uvicorn
from starlette.middleware.cors import CORSMiddleware
from api import api_root
from pydantic import BaseModel

app = FastAPI()

app.include_router(api_root, prefix="/api")


@app.get("/")
def read_root():
    return {"Hello": "you are welcome to use this api, please visit /api/docs to get more info"}


# class Item(BaseModel):
#     name: Optional[str] = None
#     price: Optional[bool] = False
#     is_offer: Optional[int] = None
from enum import Enum


class UserInfo(BaseModel):
    user_name: str
    user_id: str


# @app.get("/test")
# def read_test(
#         page: int = Query(default=0, ge=0, le=50),
#         name: str = Query(default=None, max_length=50),
#         price: bool = Query(default=False),
# ):
#     if not name:
#         return {"error": "name is must be required"}
#     data = {"page": page, "name": name, "price": price}
#     # if user_info:
#     #     if user_info.user_name  and user_info.user_id:
#     #         data.update({"user_id": user_info.user_id, "user_name": user_info.user_name})
#
#     return data


if __name__ == '__main__':
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # 设置允许访问的域名,"*"，即为所有,允许的origins来源
        allow_credentials=True,
        allow_methods=["*"],  # 设置允许跨域的http方法，比如 get、post、put等。
        allow_headers=["*"]
    )  # 允许跨域的headers，可以用来鉴别来源等作用。

    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True, debug=True)
