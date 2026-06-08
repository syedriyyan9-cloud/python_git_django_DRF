try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print(f"Result is {result}")
finally:
    print("Execution finished.")

def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive")
    if amount > balance:
        raise RuntimeError(f"Insufficient funds. Balance: {balance}")
    return balance - amount

try:
    new_balance = withdraw(100, -5)
except ValueError as e:
    print(f"Input error: {e}")
except RuntimeError as e:
    print(f"Transaction error: {e}")


data = {"name": "Alice"}
try:
    print(data["age"])          # KeyError
    num = int("ten")            # ValueError
    result = "count: " + 5      # TypeError
except KeyError:
    print("Missing dictionary key")
except ValueError:
    print("Cannot convert to integer")
except TypeError:
    print("Wrong type for operation")

