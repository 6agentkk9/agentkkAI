# Remember these three rules
# 1. I/O-bound: Start with asyncio or ThreadPoolExecutor.
# 2. CPU-bound: Consider ProcessPoolExecutor.
# 3. Shared mutable data: Think carefully about thread safety and synchronization.


from concurrent.futures import ThreadPoolExecutor
import time


def check_payment(payment_id: str) -> dict:

    print(f"Checking {payment_id}")

    # Simulate synchronous gateway API call
    time.sleep(2)

    return {
        "payment_id": payment_id,
        "status": "SUCCESS"
    }


def main():

    payment_ids = [
        "PAY-50001",
        "PAY-50002",
        "PAY-50003",
        "PAY-50004"
    ]

    start = time.perf_counter()

    with ThreadPoolExecutor(max_workers=2) as executor:

        results = list(
            executor.map(check_payment, payment_ids)
        )

    for result in results:
        print(result)

    elapsed = time.perf_counter() - start

    print(f"Total execution time: {elapsed:.2f} seconds")


if __name__ == "__main__":
    main()
