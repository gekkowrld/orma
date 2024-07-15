#!/usr/bin/pydoc3

from fastapi import FastAPI

from src.house import create_house, get_all_houses, view_house
from src.types import HouseInfo, Item
from src.user import get_all_users, get_user, post_user

app = FastAPI()


@app.get("/")
def dead_root():
    return {"msg": "This provides nothing, try /docs for available routes"}


@app.get("/user_details/{id}")
def get_user_(id):
    return get_user(id)


@app.get("/all_users")
def get_all_users_():
    return get_all_users()


@app.post("/create_user")
def post_user_(item: Item):
    return post_user(item)


@app.get("/houses")
def get_houses_():
    return get_all_houses()


@app.post("/create_house")
def create_house_(house: HouseInfo):
    return create_house(house)


@app.get("/house/{id}")
def get_house_(id):
    return view_house(id)
