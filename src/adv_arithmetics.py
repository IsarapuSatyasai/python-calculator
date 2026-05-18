# Python Advanced Arithmetics
def factorial(n):
    """Returns the factorial of n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

def fibonacci(n):
    """Returns the nth Fibonacci number."""
    if n < 0:
        raise ValueError("Fibonacci sequence is not defined for negative indices.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def gcd(a, b):
    """Returns the greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return abs(a)

if __name__ == "__main__":
    # Use these methods when it is imported as a module, not when run directly.
    pass
    