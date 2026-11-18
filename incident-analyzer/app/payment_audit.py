from contextlib import contextmanager


@contextmanager
def payment_audit():
    print("Starting payment audit")

    try:
        yield

        print("Payment audit completed")

    except Exception:
        print("Payment audit failed")
        raise

    finally:
        print("Closing audit")


with payment_audit():
    print("Checking failed payments")
    raise ValueError("Database unavailable")