def parse_expression(expression):
    parts = expression.split()
    if len(parts) == 3:
        num1 = int(parts[0])
        operator = parts[1]
        num2 = int(parts[2])

        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            return num1 / num2
    else:
        raise ValueError("Expression format is invalid.")


with open("input1b.txt", "r") as file:
    lines = file.readlines()

T = int(lines[0].strip())
expressions = [line.split("calculate ")[1].strip() for line in lines[1:T + 1]]

results = []
for expr in expressions:
    try:
        result = parse_expression(expr)
        results.append(f"The result of {expr} is {result}\n")
    except ValueError as e:
        results.append(f"Error in expression '{expr}': {e}\n")

with open("output1b.txt", "w") as output_file:
    output_file.writelines(results)
