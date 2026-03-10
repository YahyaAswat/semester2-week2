import sqlite3

db_path = r"/workspaces/semester2-week2/session_1/3_python/leeds_eats/food_delivery.db"

conn = sqlite3.connect(db_path)
query = "SELECT * FROM customers"

cursor = conn.execute(query)

for row in cursor:
    print(row)