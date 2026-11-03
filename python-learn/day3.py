print("Example 1")
try:
    amount = int("ABC")
    fee = amount / 0

except ValueError:
    print("Invalid transaction amount")

except ZeroDivisionError:
    print("Invalid calculation")

except Exception as e:
    print(f"Unexpected error: {e}")


print("Example 2")
try:
    print("Processing payment")
    result = 100 / 0

except ZeroDivisionError:
    print("Calculation failed")

finally:
    print("Closing resources")