from typing import Annotated
from urllib.request import Request
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field
from starlette.responses import JSONResponse
from datetime import datetime

app = FastAPI()


class BaseUser(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserIn(BaseUser):
    password: str


# 这里实际返回的是一个UserIn实例,但UserIn是BaseUser的子类,可以成功返回
@app.post("/user/", response_model=BaseUser, status_code=201)
async def create_user(user: UserIn) -> BaseUser:
    return user


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5
    tags: list[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}

# @app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True, status_code=200)
# async def read_item(item_id: str):
#     return items[item_id]


item_ids = ["foo", "bar", "baz"]


@app.get("/items/{item_id}")
async def get_item(item_id: str):
    if item_id not in item_ids:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        return items[item_id]


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


# 安装自定义异常处理器
@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )


# 作业
class TodoBase(BaseModel):
    name: Annotated[str, Field(min_length=1, max_length=100)]
    email: EmailStr | None = None
    created_at: datetime


class TodoCreate(TodoBase):
    password: Annotated[str, Field(min_length=6)]  # 只进不出


class TodoUpdate(BaseModel):
    name: Annotated[str, Field(min_length=1, max_length=100)] | None = None
    email: EmailStr | None = None


todos = {
    "001": {"name": "wsm", "created_at": datetime(2020, 1, 1)},
    "002": {"name": "syr", "created_at": datetime(2025, 11, 24)},
    "003": {"name": "rws", "created_at": datetime(2023, 1, 26)},
}


@app.post("/todos", status_code=201, response_model=TodoBase)
async def create_todo(todo: TodoCreate):
    new_id = f"{len(todos) + 1:03d}"
    todos[new_id] = todo.model_dump(exclude={"password"})  # 写的时候就丢掉密码
    return todos[new_id]


@app.get("/todos/{todo_id}", response_model=TodoBase)
async def get_todo(todo_id: str):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todos[todo_id]


@app.delete("/todos/{todo_id}", status_code=204)
async def delete_todo(todo_id: str) -> None:
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    del todos[todo_id]
