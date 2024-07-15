#!/usr/bin/python3

import os
import sqlite3
import uuid

from dotenv import load_dotenv

load_dotenv()

# Load the database name from environment variable or use default
DB_NAME = os.getenv("DB_NAME", "orma.db")
HOUSE_TABLE = "house"


def setup():
    """Set up the SQLite database connection and cursor."""
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    # Create the house table if it does not exist
    cur.execute(
        f"""
        CREATE TABLE IF NOT EXISTS {HOUSE_TABLE} (
            id TEXT PRIMARY KEY,
            name VARCHAR(32) NOT NULL,
            house_floor INTEGER NOT NULL,
            is_occupied BOOLEAN NOT NULL,
            is_maintenance BOOLEAN NOT NULL,
            req_no VARCHAR(32)
        )
        """
    )
    conn.commit()
    return conn, cur


def create_house(conn, name, house_floor, is_occupied, is_maintenance, req_no):
    """Create a new house in the database."""
    if any(x is None for x in [name, house_floor, is_occupied, is_maintenance, req_no]):
        return {"msg": "Some of the values entered are nil"}

    _id = str(uuid.uuid4())

    try:
        cur = conn.cursor()
        cur.execute(
            f"""
            INSERT INTO {HOUSE_TABLE} (id, name, house_floor, is_occupied, is_maintenance, req_no)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (_id, name, house_floor, is_occupied, is_maintenance, req_no),
        )
        conn.commit()
        return {"msg": "House created successfully", "id": _id}
    except sqlite3.OperationalError as e:
        return {"msg": str(e)}


def get_house(conn, house_id):
    """Retrieve a house from the database by id."""
    try:
        cur = conn.cursor()
        cur.execute(
            f"""
            SELECT id, name, house_floor, is_occupied, is_maintenance, req_no
            FROM {HOUSE_TABLE}
            WHERE id = ?
            """,
            (house_id,),
        )
        result = cur.fetchone()
        if result:
            return {"msg": result}
        return {"msg": "House not found"}
    except sqlite3.OperationalError as e:
        return {"msg": str(e)}


def get_all_houses(conn):
    """Retrieve all houses from the database."""
    try:
        cur = conn.cursor()
        cur.execute(
            f"""
            SELECT id, name, house_floor, is_occupied, is_maintenance, req_no
            FROM {HOUSE_TABLE}
            """
        )
        results = cur.fetchall()
        return {"msg": results}
    except sqlite3.OperationalError as e:
        return {"msg": str(e)}


def delete_house(conn, house_id):
    """Delete a house from the database by id."""
    try:
        cur = conn.cursor()
        cur.execute(
            f"""
            DELETE FROM {HOUSE_TABLE} WHERE id = ?
            """,
            (house_id,),
        )
        conn.commit()
        return {"msg": "Deleted successfully"}
    except sqlite3.OperationalError as e:
        return {"msg": str(e)}


def update_house(
    conn,
    house_id,
    name=None,
    house_floor=None,
    is_occupied=None,
    is_maintenance=None,
    req_no=None,
):
    """Update a house's details in the database."""
    if house_id is None:
        return {"msg": "No id provided"}

    # Create a list of columns to be updated and their values
    updates = []
    values = []
    if name is not None:
        updates.append("name = ?")
        values.append(name)
    if house_floor is not None:
        updates.append("house_floor = ?")
        values.append(house_floor)
    if is_occupied is not None:
        updates.append("is_occupied = ?")
        values.append(is_occupied)
    if is_maintenance is not None:
        updates.append("is_maintenance = ?")
        values.append(is_maintenance)
    if req_no is not None:
        updates.append("req_no = ?")
        values.append(req_no)

    if not updates:
        return {"msg": "No fields to update"}

    # Add the condition for the house id
    updates_str = ", ".join(updates)
    values.append(house_id)
    try:
        cur = conn.cursor()
        cur.execute(
            f"""
            UPDATE {HOUSE_TABLE}
            SET {updates_str}
            WHERE id = ?
            """,
            tuple(values),
        )
        conn.commit()
        return {"msg": "House updated successfully"}
    except sqlite3.OperationalError as e:
        return {"msg": str(e)}
