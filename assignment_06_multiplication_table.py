# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

SEPARATOR = "---------------------------"


def print_single_table(number):
    """PART A — print the 1 to 12 multiplication table for one number."""
    print(f"Multiplication Table for {number}:")
    for multiplier in range(1, 13):
        # ljust(2) keeps the '=' signs lined up for 1-digit and 2-digit values.
        print(f"{number}  x  {str(multiplier).ljust(2)} =  {number * multiplier}")


def print_tables_up_to(limit):
    """PART B — print a full table for every number from 1 up to 'limit'."""
    for number in range(1, limit + 1):
        print_single_table(number)
        # No separator after the very last table.
        if number != limit:
            print(SEPARATOR)


def read_positive_integer(prompt):
    """Ask for a whole number greater than 0, or return None if invalid."""
    try:
        value = int(input(prompt))
    except ValueError:
        return None

    if value <= 0:
        return None
    return value


def main():
    # ---------------- PART A ----------------
    number = read_positive_integer("Enter a number: ")
    if number is None:
        print("Error: Please enter a positive whole number.")
        return

    print()
    print_single_table(number)

    # ---------------- PART B ----------------
    print()
    limit = read_positive_integer("Enter N to print tables from 1 to N: ")
    if limit is None:
        print("Error: N must be a positive integer.")
        return

    print()
    print_tables_up_to(limit)


if __name__ == "__main__":
    main()

