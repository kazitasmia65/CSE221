def bubble_sort_optimized(arr):
    """
    Optimized Bubble Sort Algorithm
    This implementation of bubble sort has a best-case time complexity of θ(n)
    when the input array is already sorted. The optimization is achieved by
    introducing a 'swapped' flag that checks if any elements were swapped
    during each pass through the array. If no elements are swapped, the array
    is already sorted, and we can break out of the loop early.
    """
    n = len(arr)
    for i in range(n - 1):
        swapped = False  # Flag to detect any swap operation
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:  # Compare adjacent elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap if needed
                swapped = True  # A swap occurred
        if not swapped:  # If no swaps occurred, the array is sorted
            break


def string_to_int_list(string):
    """Convert a space-separated string of numbers to a list of integers."""
    int_list = []
    numbers = string.split()  # Split the string by spaces
    for num in numbers:
        int_list.append(int(num))  # Convert each number to an integer
    return int_list


def task_2():
    with open("input2.txt", "r") as f:
        lines = f.readlines()

    T = int(lines[0])  # Read the first line for number of elements
    arr = string_to_int_list(lines[1])  # Convert the second line to a list of integers

    bubble_sort_optimized(arr)  # Sort the array using optimized bubble sort

    with open("output2.txt", "w") as f:
        f.writelines(" ".join(str(x) for x in arr) + "\n")  # Write sorted array to output file


# Call the task_2 function to execute the sorting process
task_2()

