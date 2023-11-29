def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = [[], [], [], []]
    for problem in problems:
        operand1, operator, operand2 = problem.split()

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        result_length = max(len(operand1), len(operand2)) + 2
        arranged_problems[0].append(operand1.rjust(result_length))
        arranged_problems[1].append(operator + operand2.rjust(result_length - 1))
        arranged_problems[2].append('-' * result_length)

        if show_answers:
            if operator == '+':
                result = str(int(operand1) + int(operand2))
            else:
                result = str(int(operand1) - int(operand2))
            arranged_problems[3].append(result.rjust(result_length))

    arranged_problems = list(map(lambda x: '    '.join(x), arranged_problems))

    if show_answers:
        return '\n'.join(arranged_problems)
    else:
        return '\n'.join(arranged_problems[:-1])
      
    return arranged_problems