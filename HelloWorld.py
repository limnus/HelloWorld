# utils.py

# Math functions
def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """Return the quotient of a and b. Raises ZeroDivisionError if b == 0."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

# String manipulation functions
def to_upper(text):
    """Convert a string to uppercase."""
    return text.upper()

def to_lower(text):
    """Convert a string to lowercase."""
    return text.lower()

def reverse_string(text):
    """Return the reversed version of the input string."""
    return text[::-1]

def is_palindrome(text):
    """Check if a string is a palindrome (case-insensitive, ignores spaces)."""
    normalized = text.replace(" ", "").lower()
    return normalized == normalized[::-1]
