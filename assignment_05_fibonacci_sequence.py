# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def print_fibonacci_terms(how_many):
    """PART A — print the first 'how_many' terms of the Fibonacci sequence."""
    current = 0
    following = 1
    sequence = []

    for _ in range(how_many):
        sequence.append(str(current))
        # Slide the window forward: the next pair is (following, current+following).
        current, following = following, current + following

    print("Fibonacci sequence: " + " ".join(sequence))


def is_fibonacci(number):
    """PART B — return True if 'number' appears in the Fibonacci sequence."""
    if number < 0:
        return False

    current = 0
    following = 1

    # Keep generating terms until we reach or pass the number we are testing.
    while current < number:
        current, following = following, current + following

    return current == number


def main():
    # ---------------- PART A ----------------
    try:
        terms = int(input("How many terms? "))
    except ValueError:
        print("Error: N must be a positive integer.")
        return

    if terms <= 0:
        print("Error: N must be a positive integer.")
        return

    print_fibonacci_terms(terms)

    # ---------------- PART B ----------------
    print()
    try:
        number = int(input("Enter a number to check: "))
    except ValueError:
        print("Error: Please enter a whole number.")
        return

    if is_fibonacci(number):
        print(f"{number} is a Fibonacci number.")
    else:
        print(f"{number} is NOT a Fibonacci number.")


if __name__ == "__main__":
    main()

