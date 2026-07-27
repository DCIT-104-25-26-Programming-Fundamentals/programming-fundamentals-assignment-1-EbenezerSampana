# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def display_menu():
    """Print the main menu."""
    print()
    print("================================")
    print("   STUDENT RECORD SYSTEM MENU")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")


def calculate_average(scores):
    """Return the average of a list of scores, rounded to 2 decimal places."""
    if len(scores) == 0:
        return 0.0

    total = 0
    for score in scores:
        total += score

    return round(total / len(scores), 2)


def find_student(students, student_id):
    """Return the record with this ID, or None if no student matches."""
    for student in students:
        if student["id"] == student_id:
            return student
    return None


def read_scores(how_many):
    """Ask the user for 'how_many' scores and return them in a list."""
    scores = []
    for position in range(how_many):
        while True:
            try:
                score = float(input(f"Enter score {position + 1}: "))
            except ValueError:
                print("Error: Please enter a valid number.")
                continue

            if score < 0 or score > 100:
                print("Error: Score must be between 0 and 100.")
                continue

            scores.append(score)
            break
    return scores


def format_score(score):
    """Print 78.0 as '78' but keep real decimals such as '78.5'."""
    if score == int(score):
        return str(int(score))
    return str(score)


def add_student(students):
    """Collect one student's details and store them as a dictionary."""
    name = input("Student name: ").strip()
    if name == "":
        print("Error: The name cannot be empty.")
        return

    try:
        student_id = int(input("Student ID: "))
    except ValueError:
        print("Error: The student ID must be a whole number.")
        return

    # IDs must stay unique so option 3 can find exactly one student.
    if find_student(students, student_id) is not None:
        print(f"Error: A student with ID {student_id} already exists.")
        return

    try:
        how_many = int(input("How many scores? "))
    except ValueError:
        print("Error: Please enter a whole number.")
        return

    if how_many <= 0:
        print("Error: You must enter at least one score.")
        return

    student = {
        "name": name,
        "id": student_id,
        "scores": read_scores(how_many),
    }

    students.append(student)
    print(f'Student "{name}" added successfully.')


def display_all_students(students):
    """Print every student in a formatted table."""
    if len(students) == 0:
        print("No students have been added yet.")
        return

    line = "-" * 50
    print(line)
    print(f"{'Name':<15}{'ID':<12}{'Scores':<15}{'Average'}")
    print(line)

    for student in students:
        # Turn [78, 85, 90] into the text "78, 85, 90".
        score_texts = []
        for score in student["scores"]:
            score_texts.append(format_score(score))
        scores_column = ", ".join(score_texts)

        average = calculate_average(student["scores"])
        print(
            f"{student['name']:<15}{student['id']:<12}"
            f"{scores_column:<15}{average}"
        )

    print(line)


def show_student_average(students):
    """Look up one student by ID and print their average score."""
    if len(students) == 0:
        print("No students have been added yet.")
        return

    try:
        student_id = int(input("Enter student ID: "))
    except ValueError:
        print("Error: The student ID must be a whole number.")
        return

    student = find_student(students, student_id)

    if student is None:
        print(f"Error: No student found with ID {student_id}.")
        return

    average = calculate_average(student["scores"])
    print(f"{student['name']}'s average score: {average}")


def main():
    students = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_all_students(students)
        elif choice == "3":
            show_student_average(students)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()

