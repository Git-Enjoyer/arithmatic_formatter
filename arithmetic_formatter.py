def arithmetic_arranger(problems, display_answers=False):
    # Check if the number of problems is more than 5, if so return an error message
    if len(problems) > 5:
        return 'Error: Too many problems.'

    # Initialize strings for each line of the output
    top_line = ""
    bottom_line = ""
    dashes_line = ""
    answers_line = ""

    # Loop through each arithmetic problem provided in the list
    for problem in problems:
        # Split the problem into components (number, operator, number)
        parts = problem.split()

        # Check if the operator is either '+' or '-'
        if parts[1] not in '+-':
            return "Error: Operator must be '+' or '-'."

        # Convert numbers to integers and handle any ValueError if numbers are not digits
        try:
            num1 = int(parts[0])
            num2 = int(parts[2])
        except ValueError:
            return "Error: Numbers must only contain digits."

        # Check if any number has more than four digits
        if len(parts[0]) > 4 or len(parts[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Calculate the width needed for the longest part plus two for spacing
        length = max(len(parts[0]), len(parts[2])) + 2

        # Format the numbers with the appropriate spacing
        top = f"{parts[0]:>{length}}"
        bottom = f"{parts[1]} {parts[2]:>{length-2}}"
        line = '-' * length

        # Optionally calculate and format the answer based on the operator
        if display_answers:
            if parts[1] == '+':
                answer = num1 + num2
            else:
                answer = num1 - num2
            answers = f"{answer:>{length}}"

        # Append spaces between problems if not the first problem
        if top_line:
            top_line += "    "  # Space between problems
            bottom_line += "    "
            dashes_line += "    "
            if display_answers:
                answers_line += "    "

        # Append each part to its corresponding line
        top_line += top
        bottom_line += bottom
        dashes_line += line
        if display_answers:
            answers_line += answers

    # Compile the final output
    arranged_problems = [top_line, bottom_line, dashes_line]
    if display_answers:
        arranged_problems.append(answers_line)

    # Join all parts with new lines and return the final arranged string
    return '\n'.join(arranged_problems)

# Test the function with and without displaying answers
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], display_answers=True))
