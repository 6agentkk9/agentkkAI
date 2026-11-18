
import asyncio
import time


async def check_payment(payment_id: str) -> dict:

    print(f"Checking {payment_id}")

    # Simulate network latency
    await asyncio.sleep(2)

    return {
        "payment_id": payment_id,
        "status": "SUCCESS"
    }


async def main():

    payment_ids = [
        "PAY-50001",
        "PAY-50002",
        "PAY-50003"
    ]

    start = time.perf_counter()

    results = await asyncio.gather(
        *[
            check_payment(payment_id)
            for payment_id in payment_ids
        ]
    )

    for result in results:
        print(result)

    elapsed = time.perf_counter() - start

    print(f"Total execution time: {elapsed:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
