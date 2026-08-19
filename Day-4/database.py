import sqlite3


connection = sqlite3.connect("company.db")

cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    product TEXT NOT NULL,
    amount REAL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
)
""")


cursor.execute("DELETE FROM orders")
cursor.execute("DELETE FROM users")


users = [
    (1, "Mukhil", "mukhil@gmail.com"),
    (2, "Arun", "arun@gmail.com"),
    (3, "Ravi", "ravi@gmail.com"),
    (4, "Karthik", "karthik@gmail.com")
]


orders = [
    (101, 1, "Laptop", 50000),
    (102, 1, "Mouse", 1000),
    (103, 2, "Keyboard", 2000),
    (104, 2, "Monitor", 15000),
    (105, 3, "Headphones", 3000),
    (106, 4, "Laptop", 55000)
]


cursor.executemany("""
INSERT INTO users (user_id, name, email)
VALUES (?, ?, ?)
""", users)


cursor.executemany("""
INSERT INTO orders (order_id, user_id, product, amount)
VALUES (?, ?, ?, ?)
""", orders)


connection.commit()


print("\n1. SELECT - Display all users")

cursor.execute("""
SELECT * FROM users
""")

print(cursor.fetchall())


print("\n2. SELECT - Display names and emails")

cursor.execute("""
SELECT name, email
FROM users
""")

print(cursor.fetchall())


print("\n3. WHERE - Find user with ID 1")

cursor.execute("""
SELECT *
FROM users
WHERE user_id = 1
""")

print(cursor.fetchall())


print("\n4. WHERE - Find orders above 10000")

cursor.execute("""
SELECT *
FROM orders
WHERE amount > 10000
""")

print(cursor.fetchall())


print("\n5. ORDER BY - Sort users by name")

cursor.execute("""
SELECT *
FROM users
ORDER BY name ASC
""")

print(cursor.fetchall())


print("\n6. ORDER BY - Sort orders by amount")

cursor.execute("""
SELECT *
FROM orders
ORDER BY amount DESC
""")

print(cursor.fetchall())


print("\n7. GROUP BY - Count orders for each user")

cursor.execute("""
SELECT user_id, COUNT(*) AS order_count
FROM orders
GROUP BY user_id
""")

print(cursor.fetchall())


print("\n8. GROUP BY - Calculate total amount for each user")

cursor.execute("""
SELECT user_id, SUM(amount) AS total_amount
FROM orders
GROUP BY user_id
""")

print(cursor.fetchall())


print("\n9. INNER JOIN - Display users and their orders")

cursor.execute("""
SELECT users.name, orders.product, orders.amount
FROM users
INNER JOIN orders
ON users.user_id = orders.user_id
""")

print(cursor.fetchall())


print("\n10. INNER JOIN - Display user name and order details")

cursor.execute("""
SELECT
    users.user_id,
    users.name,
    orders.order_id,
    orders.product,
    orders.amount
FROM users
INNER JOIN orders
ON users.user_id = orders.user_id
ORDER BY users.user_id
""")

print(cursor.fetchall())


connection.close()