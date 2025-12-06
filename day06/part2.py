import re

# with open('input.txt') as f:
with open('example.txt') as f:
    lines = f.readlines()

def split_line(line):
    result = []
    for i in range(0, len(line), 4):
        result.append(line[i:i+3])
    return result

table = []
# Regular lines
for l in lines[:-1]:
    line_split = split_line(l)
    line_zeroes = [i.replace(' ', '0') for i in line_split]
    table.append(line_zeroes)
# Last line containing operators
table.append(re.split(r'\s+', lines[-1].strip()))

transposed = []
for column_idx in range(len(table)):
    column_buffer = []
    for row_idx in range(len(table[0])):
        column_buffer.append(table[row_idx][column_idx])
    transposed.append(column_buffer)

print(transposed)

# 123 328  51 64 
#  45 64  387 23 
#   6 98  215 314
# *   +   *   + 

# The rightmost problem is 4 + 431 + 623 = 1058
# The second problem from the right is 175 * 581 * 32 = 3253600
# The third problem from the right is 8 + 248 + 369 = 625
# Finally, the leftmost problem is 356 * 24 * 1 = 8544


first_colum = transposed[0]
op = first_colum[-1]

# Create number for each 'internal' colum, e.g. 356
def assemble_vertical_number(external_column, internal_column_idx):
    result = 0
    i=internal_column_idx
    exponent = 0
    for row_idx, elem in enumerate(reversed(external_column)):
        digit=elem[i]
        value = int(digit) * eval(f"1e{exponent}")
        if int(digit) != 0:
            exponent += 1
        result += value
    return result

result = 0

for col in transposed:
    op = col[-1]

    if op == '*':
        accu = 1
    else:
        accu = 0

    for idx in range(3):
        value = assemble_vertical_number(col[:-1], idx)
        accu = eval(f"accu {op} value")

    result += accu

print(int(result))
