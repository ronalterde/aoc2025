import re

values = []
with open('input.txt') as f:
# with open('example.txt') as f:
    for line in f:
        line_split = re.split(r'\s+', line.strip())
        values.append(line_split)

sum = 0
for column in range(len(values[0])):
    expression = ''
    for row in range(len(values)):
        value = values[row][column]
        if value == '+' or value == '*':
            operator = value
            expression = expression.strip()
            expression = expression.replace(' ', operator)
            sum += eval(expression)
        else:
            expression += value + " "

print(sum)

