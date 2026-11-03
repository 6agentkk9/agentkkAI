# Full exercise - read a csv file, filter the data and write to a new file

transactions = [
    "1001,SUCCESS,250",
    "1002,FAILED,150",
    "1003,SUCCESS,300",
    "1004,FAILED,400"
]

# with open("failed_report.txt", "w") as file:   point to G:\agentkkAI

# point to G:\agentkkAI\python-learn  current path
from pathlib import Path
report_path = Path(__file__).with_name("failed_report.txt")
with open(report_path, "w") as file:


    file.write("Failed Payment Report\n")

    for transaction in transactions:

        transaction_id, status, amount = (
            transaction.split(",")
        )

        if status == "FAILED":
            file.write(
                f"{transaction_id} - {amount}\n"
            )