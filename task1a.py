with open("input1a.txt", "r") as file:
    lines = file.readlines()

N = int(lines[0].strip())
results = []

for i in range(1, N + 1):
    curr = int(lines[i].strip())
    if curr % 2 == 0:
        results.append(f"{curr} is an Even number.\n")
    else:
        results.append(f"{curr} is an Odd number.\n")

# Write the results to output1a.txt
with open("output1a.txt", "w") as output_file:
    output_file.writelines(results)
