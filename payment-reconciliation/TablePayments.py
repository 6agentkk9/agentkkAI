import sqlite3


from pathlib import Path
db_path = Path(__file__).with_name("payments.db")

connection = sqlite3.connect(db_path)

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS payments (
        payment_id INTEGER PRIMARY KEY,
        amount REAL,
        status TEXT
    )
""")

cursor.execute("""
    INSERT INTO payments (payment_id, amount, status)
    VALUES (1001, 250.50, 'SUCCESS')
""")

cursor.execute("""
    INSERT INTO payments (payment_id, amount, status)
    VALUES (1002, 175.00, 'FAILED')
""")

connection.commit()
connection.close()