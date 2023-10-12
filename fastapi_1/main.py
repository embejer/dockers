from typing import Union
from os import environ as env


from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root():
    print(f"{env.get('SECRET_MESSAGE')}")
    return {"message": f"{env.get('SECRET_MESSAGE')}"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
