#!/usr/bin/python3

import os
import sqlite3
import uuid

from dotenv import load_dotenv

load_dotenv()

# Load the database name from environment variable or use default
DB_NAME = os.getenv("DB_NAME", "orma.db")
USER_TABLE = "users"


def setup():
    """Set up the SQLite database connection and cursor."""
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    # Create the user table if it does not exist
    cur.execute(
        f"""
        CREATE TABLE IF NOT EXISTS {USER_TABLE} (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            id_no INTEGER NOT NULL,
            phone_number INTEGER NOT NULL,
            house_number VARCHAR(32) NOT NULL
        )
        """
    )
    conn.commit()
    return conn, cur


def create_user(conn, name, id_no, phone_number, house_number):
    """Create a new user in the database."""
    if not all([name, id_no, phone_number, house_number]):
        return {"msg": "Some of the values entered are nil"}

    _id = str(uuid.uuid4())

    try:
        cur = conn.cursor()
        cur.execute(
            f"""
            INSERT INTO {USER_TABLE} (id, name, id_no, phone_number, house_number)
            VALUES (?, ?, ?, ?, ?)
            """,
            (_id, name, id_no, phone_number, house_number),
        )
        conn.commit()
        return {"msg": "User created successfully", "id": _id}
    except sqlite3.OperationalError as e:
        return {"msg": str(e)}


def get_user(cur, user_id):
    """Retrieve a user from the database by id."""
    try:
        cur.execute(
            f"""
            SELECT id, name, id_no, phone_number, house_number
            FROM {USER_TABLE}
            WHERE id = ?
            """,
            (user_id,),
        )
        result = cur.fetchone()
        if result:
            return {"msg": result}
        return {"msg": "User not found"}
    except sqlite3.OperationalError as e:
        return {"msg": str(e)}


def get_all_users(cur):
    """Retrieve all users from the database."""
    try:
        cur.execute(
            f"""
            SELECT id, name, id_no, phone_number, house_number
            FROM {USER_TABLE}
            """
        )
        results = cur.fetchall()
        return {"msg": results}
    except sqlite3.OperationalError as e:
        return {"msg": str(e)}


def delete_user(conn, user_id):
    """Delete a user from the database by id."""
    try:
        cur = conn.cursor()
        cur.execute(
            f"""
            DELETE FROM {USER_TABLE} WHERE id = ?
            """,
            (user_id,),
        )
        conn.commit()
        return {"msg": "Deleted successfully"}
    except sqlite3.OperationalError as e:
        return {"msg": str(e)}


def update_user(conn, user_id, id_no=None, phone_number=None, house_number=None):
    """Update a user's details in the database."""
    if user_id is None:
        return {"msg": "No id provided"}

    # Build the SET clause for the update statement
    update_clause = []
    params = []
    if id_no is not None:
        update_clause.append("id_no = ?")
        params.append(id_no)
    if phone_number is not None:
        update_clause.append("phone_number = ?")
        params.append(phone_number)
    if house_number is not None:
        update_clause.append("house_number = ?")
        params.append(house_number)

    if not update_clause:
        return {"msg": "No update fields provided"}

    # Append the user_id for the WHERE clause
    update_clause_str = ", ".join(update_clause)
    params.append(user_id)

    try:
        cur = conn.cursor()
        cur.execute(
            f"""
            UPDATE {USER_TABLE}
            SET {update_clause_str}
            WHERE id = ?
            """,
            tuple(params),
        )
        conn.commit()
        return {"msg": "User updated successfully"}
    except sqlite3.OperationalError as e:
        return {"msg": str(e)}
