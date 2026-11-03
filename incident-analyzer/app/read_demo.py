if __package__:
    from .database import get_connection
else:
    from database import get_connection

def read_incidents():

    with get_connection() as connection:
        rows = connection.execute("""
            SELECT *
            FROM payment_incidents
            WHERE status = ?
            ORDER BY incident_id
        """,("FAILED",)).fetchall()

    for row in rows:
        print(dict(row))


if __name__ == "__main__":
    read_incidents()