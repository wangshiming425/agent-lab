from typing import Annotated, List
from fastapi import FastAPI, Query
from enum import Enum
from pydantic import BaseModel,Field

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


# 请求体参数使用
class User(BaseModel):
    username: str
    email: str | None = None
    password: str


@app.get("/users/")
async def get_users(user: User):
    return user.dict()


@app.get("/items/")
async def get_items(
    skip: Annotated[int, Query(ge=0, description="跳过记录数")] = 0,
    limit: Annotated[int, Query(ge=1, le=100, description="每页条数")] = 10,
    q: Annotated[str, Query(description="查询条件", max_length=50)] = "",
):
    return {"skip": skip, "limit": limit, "q": q}

class ItemCreate(BaseModel):
    username: Annotated[str, Field(min_length=1, max_length=100)]    # 想强制必填就去掉 = ""
    price: Annotated[float, Field(gt=0)]                                  # 无默认值 → 必填
    tags: list[str]                                                       # 必填

@app.post("/items/")
async def create_item(item: ItemCreate):
    return {"item": item}