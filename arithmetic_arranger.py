def arithmetic_arranger(problems, show_answers=False):
  if len(problems) > 5:
    return "Error: Too many problems"

  arranged_problems = {"top": [], "bottom": [], "operator": [], "line": []}

  for problem in problems:
    elements = problem.split()
    num1, operator, num2 = elements[0], elements[1], elements[2]

    if operator not in ["+", "-"]:
      return "Error: Operator must be '+' or '-'"

    if not num1.isdigit() or not num2.isdigit():
      return "Error: Numbers must only contain digits"

    if len(num1) > 4 or len(num2) > 4:
      return "Error: Numbers cannot be more than four digits"

    width = max(len(num1), len(num2)) + 2
    arranged_problems["top"].append(num1.rjust(width))
    arranged_problems["bottom"].append(operator + num2.rjust(width - 1))
    arranged_problems["operator"].append("-" * width)

    if show_answers:
      if operator == "+":
        result = str(int(num1) + int(num2))
      else:
        result = str(int(num1) - int(num2))
      arranged_problems["line"].append(result.rjust(width))

  arranged_format = [
      "    ".join(arranged_problems["top"]),
      "    ".join(arranged_problems["bottom"]),
      "    ".join(arranged_problems["operator"])
  ]

  if show_answers:
    arranged_format.append("    ".join(arranged_problems["line"]))

  return "\n".join(arranged_format)
