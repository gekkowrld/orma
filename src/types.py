#!/usr/bin/python3

from pydantic import BaseModel


class HouseInfo(BaseModel):
    name: str
    floor: int
    is_occupied: bool
    is_maintenance: bool
    req_no: str  # For the maintanance request


class Item(BaseModel):
    name: str
    id_no: int
    phone_number: int
    house_number: str
