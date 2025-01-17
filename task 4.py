def parse_time(time_str):
    """Parse time in "HH:MM" format and convert it into minutes since midnight."""
    hours, minutes = map(int, time_str.split(":"))
    return hours * 60 + minutes  # Convert to total minutes for easier comparison


def bubble_sort_trains(trains):
    """Sort the trains based on name, latest departure time, and input order using bubble sort."""
    n = len(trains)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Compare lexicographically by name
            if (trains[j][0] > trains[j + 1][0]) or \
                    (trains[j][0] == trains[j + 1][0] and trains[j][1] < trains[j + 1][1]):
                trains[j], trains[j + 1] = trains[j + 1], trains[j]  # Swap if needed


def task_4():
    with open("input4.txt", "r") as f:
        lines = f.readlines()

    N = int(lines[0].strip())  # Read the number of trains

    trains = []
    for i in range(1, N + 1):
        line = lines[i].strip()
        # Extract train name and departure time
        name_part = line.split(" will departure for ")[0]
        time_part = line.split(" at ")[-1]

        departure_time = parse_time(time_part)  # Convert time to total minutes
        trains.append((name_part, departure_time, line))  # Store as tuple (name, departure_time, original line)

    bubble_sort_trains(trains)  # Sort the trains using bubble sort

    # Prepare output lines based on sorted trains
    results = [train[2] + "\n" for train in trains]  # Use the original line for output

    with open("output4.txt", "w") as f:
        f.writelines(results)  # Write the sorted schedule to output file


# Call the task_4 function to execute the train scheduling process
task_4()
