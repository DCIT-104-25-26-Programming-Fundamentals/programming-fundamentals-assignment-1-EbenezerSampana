# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def calculate_sum(numbers):
    """Add up every value in the list without using the built-in sum()."""
    total = 0
    for value in numbers:
        total += value
    return total


def calculate_average(numbers):
    """Return the average of the list (sum divided by how many values)."""
    return calculate_sum(numbers) / len(numbers)


def find_maximum(numbers):
    """Return the largest value without using the built-in max()."""
    largest = numbers[0]
    for value in numbers:
        if value > largest:
            largest = value
    return largest


def find_minimum(numbers):
    """Return the smallest value without using the built-in min()."""
    smallest = numbers[0]
    for value in numbers:
        if value < smallest:
            smallest = value
    return smallest


def format_number(value):
    """Print 23.0 as '23' but keep real decimals such as '4.6'."""
    if value == int(value):
        return str(int(value))
    return str(round(value, 2))


def read_numbers(how_many):
    """Ask the user for 'how_many' numbers and return them in a list."""
    numbers = []
    for position in range(how_many):
        while True:
            try:
                value = float(input(f"Enter number {position + 1}: "))
                break
            except ValueError:
                print("Error: Please enter a valid number.")
        numbers.append(value)
    return numbers


def main():
    try:
        count = int(input("How many numbers? "))
    except ValueError:
        print("Error: N must be a positive integer.")
        return

    if count <= 0:
        print("Error: N must be a positive integer.")
        return

    numbers = read_numbers(count)

    print()
    print("Results:")
    print(f"{'Sum:':<9}{format_number(calculate_sum(numbers))}")
    print(f"{'Average:':<9}{format_number(calculate_average(numbers))}")
    print(f"{'Maximum:':<9}{format_number(find_maximum(numbers))}")
    print(f"{'Minimum:':<9}{format_number(find_minimum(numbers))}")


if __name__ == "__main__":
    main()
