def arithmetic_arranger(problems, show_answers=False):
    # Check if there are too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = ""
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

    for problem in problems:
        parts = problem.split()
        num1, operator, num2 = parts[0], parts[1], parts[2]

        # Check for valid operator
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        # Check for valid operands
        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."

        # Check for max operand width
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Calculate the maximum width for alignment
        max_width = max(len(num1), len(num2)) + 2

        # Create the formatted strings for each line
        line1 += num1.rjust(max_width)
        line2 += operator + num2.rjust(max_width - 1)
        line3 += "-" * max_width
        result = str(eval(problem)) if show_answers else ""
        line4 += result.rjust(max_width)

        if problem != problems[-1]:
            line1 += "    "
            line2 += "    "
            line3 += "    "
            line4 += "    "

    arranged_problems += line1 + "\n" + line2 + "\n" + line3
    if show_answers:
        arranged_problems += "\n" + line4

    return arranged_problems

problems1 = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
print(arithmetic_arranger(problems1))

problems2 = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
print(arithmetic_arranger(problems2, True))
