import sqlite3

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()


class User(BaseModel):
    name: str
    email: str


def get_connection():
    connection = sqlite3.connect("company.db")
    connection.row_factory = sqlite3.Row
    return connection


@app.get("/")
def home():
    return {
        "message": "Welcome to Day 4 FastAPI"
    }


@app.get("/about")
def about():
    return {
        "message": "FastAPI with SQLite database"
    }


@app.get("/users")
def get_users():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    SELECT *
    FROM users
    """)

    users = cursor.fetchall()

    connection.close()

    return [dict(user) for user in users]


@app.get("/users/{user_id}")
def get_user(user_id: int):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    SELECT *
    FROM users
    WHERE user_id = ?
    """, (user_id,))

    user = cursor.fetchone()

    connection.close()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return dict(user)


@app.get("/orders/{user_id}")
def get_user_orders(user_id: int):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    SELECT
        orders.order_id,
        users.name,
        orders.product,
        orders.amount
    FROM orders
    INNER JOIN users
    ON users.user_id = orders.user_id
    WHERE users.user_id = ?
    """, (user_id,))

    orders = cursor.fetchall()

    connection.close()

    if not orders:
        raise HTTPException(
            status_code=404,
            detail="No orders found for this user"
        )

    return [dict(order) for order in orders]


@app.post("/users")
def create_user(user: User):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
        INSERT INTO users (name, email)
        VALUES (?, ?)
        """, (user.name, user.email))

        connection.commit()

        user_id = cursor.lastrowid

        connection.close()

        return {
            "message": "User created successfully",
            "user_id": user_id,
            "name": user.name,
            "email": user.email
        }

    except sqlite3.IntegrityError:
        connection.close()

        raise HTTPException(
            status_code=409,
            detail="Email already exists"
        )