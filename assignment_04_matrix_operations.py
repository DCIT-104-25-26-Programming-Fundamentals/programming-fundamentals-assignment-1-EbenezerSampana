# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def read_size(prompt):
    """Keep asking until the user gives a whole number greater than 0."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Error: Please enter a whole number.")
            continue

        if value <= 0:
            print("Error: The value must be greater than 0.")
            continue

        return value


def read_matrix(rows, columns, name=""):
    """Read a rows x columns matrix, one row per line, values separated by spaces."""
    if name:
        print(f"Enter the values for matrix {name}:")

    matrix = []
    for row_number in range(rows):
        while True:
            parts = input(f"Enter row {row_number + 1}: ").split()

            if len(parts) != columns:
                print(f"Error: Please enter exactly {columns} values.")
                continue

            row = []
            valid = True
            for part in parts:
                try:
                    row.append(int(part))
                except ValueError:
                    print("Error: All values must be whole numbers.")
                    valid = False
                    break

            if valid:
                matrix.append(row)
                break

    return matrix


def display_matrix(matrix, title):
    """Print a matrix as a neat, right-aligned grid."""
    print(title)

    # Find the widest value so every column can share the same width.
    width = 1
    for row in matrix:
        for value in row:
            if len(str(value)) > width:
                width = len(str(value))

    for row in matrix:
        line = ""
        for value in row:
            line += str(value).rjust(width) + "  "
        print(line.rstrip())


def transpose_matrix(matrix):
    """PART A — swap rows and columns: element [i][j] becomes [j][i]."""
    rows = len(matrix)
    columns = len(matrix[0])

    result = []
    for column in range(columns):
        new_row = []
        for row in range(rows):
            new_row.append(matrix[row][column])
        result.append(new_row)

    return result


def add_matrices(matrix_a, matrix_b):
    """PART B — add two matrices of the same size, position by position."""
    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        return None

    result = []
    for row in range(len(matrix_a)):
        new_row = []
        for column in range(len(matrix_a[0])):
            new_row.append(matrix_a[row][column] + matrix_b[row][column])
        result.append(new_row)

    return result


def multiply_matrices(matrix_a, matrix_b):
    """PART C — multiply an M x N matrix by an N x P matrix, giving M x P."""
    # The columns of A must match the rows of B.
    if len(matrix_a[0]) != len(matrix_b):
        return None

    rows = len(matrix_a)
    shared = len(matrix_b)
    columns = len(matrix_b[0])

    result = []
    for row in range(rows):
        new_row = []
        for column in range(columns):
            # Each result cell is the running total of row x column products.
            total = 0
            for position in range(shared):
                total += matrix_a[row][position] * matrix_b[position][column]
            new_row.append(total)
        result.append(new_row)

    return result


def part_a():
    print("=" * 45)
    print("PART A — TRANSPOSE A MATRIX")
    print("=" * 45)

    rows = read_size("Enter number of rows: ")
    columns = read_size("Enter number of columns: ")
    matrix = read_matrix(rows, columns)

    print()
    display_matrix(matrix, "Original Matrix:")
    print()
    display_matrix(transpose_matrix(matrix), "Transposed Matrix:")


def part_b():
    print()
    print("=" * 45)
    print("PART B — ADD TWO MATRICES")
    print("=" * 45)

    rows = read_size("Enter number of rows: ")
    columns = read_size("Enter number of columns: ")

    matrix_a = read_matrix(rows, columns, "A")
    matrix_b = read_matrix(rows, columns, "B")

    result = add_matrices(matrix_a, matrix_b)

    print()
    display_matrix(matrix_a, "Matrix A:")
    print()
    display_matrix(matrix_b, "Matrix B:")
    print()

    if result is None:
        print("Error: Both matrices must be the same size.")
    else:
        display_matrix(result, "Sum (A + B):")


def part_c():
    print()
    print("=" * 45)
    print("PART C — MULTIPLY TWO MATRICES")
    print("=" * 45)

    rows = read_size("Enter number of rows for matrix A (M): ")
    shared = read_size("Enter number of columns for A / rows for B (N): ")
    columns = read_size("Enter number of columns for matrix B (P): ")

    matrix_a = read_matrix(rows, shared, "A")
    matrix_b = read_matrix(shared, columns, "B")

    result = multiply_matrices(matrix_a, matrix_b)

    print()
    display_matrix(matrix_a, "Matrix A:")
    print()
    display_matrix(matrix_b, "Matrix B:")
    print()

    if result is None:
        print("Error: Columns of A must equal rows of B.")
    else:
        display_matrix(result, "Product (A x B):")


def main():
    part_a()
    part_b()
    part_c()


if __name__ == "__main__":
    main()
