def string_to_int_list(string):
    """Convert a space-separated string of numbers to a list of integers."""
    int_list = []
    numbers = string.split()  # Split the string by spaces
    for num in numbers:
        int_list.append(int(num))  # Convert each number to an integer
    return int_list


def bubble_sort_students(student_data):
    """Sort the students based on marks and IDs using bubble sort."""
    n = len(student_data)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Compare marks, and in case of a tie, compare IDs
            if (student_data[j][1] < student_data[j + 1][1]) or \
                    (student_data[j][1] == student_data[j + 1][1] and student_data[j][0] > student_data[j + 1][0]):
                student_data[j], student_data[j + 1] = student_data[j + 1], student_data[j]  # Swap


def task_3():
    with open("input3.txt", "r") as f:
        lines = f.readlines()

    N = int(lines[0])  # Read the number of students
    student_ids = string_to_int_list(lines[1])  # Convert the second line to a list of student IDs
    marks = string_to_int_list(lines[2])  # Convert the third line to a list of marks

    # Combine student IDs and marks into a list of tuples
    student_data = []
    for i in range(N):
        student_data.append((student_ids[i], marks[i]))  # Create a tuple for each student

    bubble_sort_students(student_data)  # Sort the students using bubble sort

    results = []
    for student in student_data:
        results.append(f"ID: {student[0]} Mark: {student[1]}\n")  # Format the results

    with open("output3.txt", "w") as f:
        f.writelines(results)  # Write the formatted results to output file


# Call the task_3 function to execute the ranking process
task_3()
