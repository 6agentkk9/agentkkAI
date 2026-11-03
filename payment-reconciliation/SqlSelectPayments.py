# Now retrieve payment records:

# Retrieve records using SELECT
import sqlite3
from pathlib import Path

#db_path = Path(__file__).with_name("payments.db") 
db_path = Path.cwd() / "payment-reconciliation" / "payments.db"

connection = sqlite3.connect(db_path)

cursor = connection.cursor()

cursor.execute("""
    SELECT payment_id, amount, status
    FROM payments
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()


# Retrieve records as dictionaries
import sqlite3
from pathlib import Path
db_path = Path.cwd() / "payment-reconciliation" / "payments.db"
connection = sqlite3.connect(db_path)

connection.row_factory = sqlite3.Row

cursor = connection.cursor()

cursor.execute("""
    SELECT payment_id, amount, status
    FROM payments
""")

rows = cursor.fetchall()

for row in rows:
    print(row["payment_id"])
    print(row["amount"])
    print(row["status"])

connection.close()