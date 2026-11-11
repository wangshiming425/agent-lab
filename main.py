from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# 路径参数的使用
# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}

# 使用有预定义值的路径参数Enum
class Items(str, Enum):
    FOO = "foo"
    BAR = "bar"


@app.get("/items/{item}")
async def get_item(item: Items):
    if item == Items.FOO:
        return {"item": item}
    elif item.value == "bar":
        return {"item": item}


# 查询参数使用
@app.get("/items/")
async def get_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}
#请求体参数使用
class User(BaseModel):
    username: str
    email: str | None = None
    password: str
@app.get("/users/")
async def get_users(user: User):
    return user.dict()
