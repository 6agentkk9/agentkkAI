# Create a Python program that:
# 1. Connects to payments.db.
# 2. Retrieves payments with status FAILED.
# 3. Prints their payment ID and amount.
# 4. Uses a parameterized SQL query.

import sqlite3
from pathlib import Path
db_path = Path.cwd() / "payment-reconciliation" / "payments.db"
connection = sqlite3.connect(db_path)
connection.row_factory = sqlite3.Row

cursor = connection.cursor()

cursor.execute(
    """
    SELECT payment_id, amount
    FROM payments
    WHERE status = ?
    """,
    ("FAILED",)
)

rows = cursor.fetchall()

for row in rows:
    print(
        f"Payment ID: {row['payment_id']}, "
        f"Amount: {row['amount']}"
    )

connection.close()