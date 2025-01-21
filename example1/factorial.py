import sys

def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n > 1:
        return n * factorial(n - 1)
    else:
        raise ValueError("Factorial is only defined for non-negative integers.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python factorial.py <number>")
        sys.exit(1)

    try:
        num = int(sys.argv[1])
        print(f"The factorial of {num} is {factorial(num)}")
    except ValueError as e:
        print(f"Error: {e}")

