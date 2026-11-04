# comment - Python will auto close the file even in exception, r = read, w = write, a = append
with open("payments.txt", "r") as file:
    for line in file:
        print(line.strip())

# loading the entire file - try to avoid this for large files
with open("payments.txt", "r") as file:
    content = file.read()

print(content)

# Python has a built-in csv module.
import csv

with open("transactions.csv", "r", newline="") as file:

    reader = csv.DictReader(file)

    for row in reader:
        print(row["transaction_id"])
        print(row["amount"])
        print(row["status"])

# exception handling - try, except, finally
try:
    with open("missing.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File does not exist")

except PermissionError:
    print("Permission denied")


# writing to a file
with open("report.txt", "w") as file:
    file.write("Daily Payment Report\n")
    file.write("Total Transactions: 100\n")
    file.write("Successful: 95\n")
    file.write("Failed: 5\n")


# impporting the Path class from pathlib module
from pathlib import Path

file_path = Path("reports") / "payments.txt"

print(file_path.exists())
print(file_path.name)
print(file_path.suffix)


# Full exercise - read a csv file, filter the data and write to a new file
transactions = [
    "1001,SUCCESS,250",
    "1002,FAILED,150",
    "1003,SUCCESS,300",
    "1004,FAILED,400"
]

with open("failed_report.txt", "w") as file:

    file.write("Failed Payment Report\n")

    for transaction in transactions:

        transaction_id, status, amount = (
            transaction.split(",")
        )

        if status == "FAILED":
            file.write(
                f"{transaction_id} - {amount}\n"
            )