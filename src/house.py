#!/usr/bin/python3

from src.db_house import create_house as ch
from src.db_house import get_all_houses as gah
from src.db_house import setup, get_house
from src.types import HouseInfo


def get_all_houses():
    conn, _ = setup()
    return gah(conn)


def create_house(house: HouseInfo):
    conn, _ = setup()
    return ch(
        conn,
        name=house.name,
        house_floor=house.floor,
        is_occupied=house.is_occupied,
        is_maintenance=house.is_maintenance,
        req_no=house.req_no,
    )


def view_house(id):
    conn, _ = setup()
    return get_house(conn, house_id=id)
