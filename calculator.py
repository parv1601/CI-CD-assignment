# calculator.py
def add(x, y):
    """Adds two numbers."""
    return x + y

def subtract(x, y):
    """Subtracts two numbers."""
    return x - y

def multiply(x, y):
    """Multiplies two numbers."""
    return x * y

def divide(x, y):
    """Divides two numbers. Handles division by zero."""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

if __name__ == "__main__":
    print("Simple CLI Calculator")
    a = 10
    b = 5
    print(f"Adding {a} + {b} = {add(a, b)}")
    print(f"Subtracting {a} - {b} = {subtract(a, b)}")