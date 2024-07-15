#!/usr/bin/python3

from src.db_user import create_user as cu
from src.db_user import get_all_users as gau
from src.db_user import get_user as gu
from src.db_user import setup
from src.types import Item


def get_user(id):
    _, cur = setup()
    return gu(cur, id)


def post_user(item: Item):
    conn, _ = setup()
    return cu(conn, item.name, item.id_no, item.phone_number, item.house_number)


def get_all_users():
    _, cur = setup()
    return gau(cur)
