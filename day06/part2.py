import re

with open('input.txt') as f:
# with open('example.txt') as f:
    lines = f.readlines()

# >>> use operators to determine beginning of each field!
field_start_positions = []
for idx, i in enumerate(lines[-1].strip()):
    if i != " ":
        field_start_positions.append(idx)
field_start_positions.append(max([len(line) for line in lines]))

def split_line(line):
    result = []
    for i in range(len(field_start_positions)-1):
        elem_value = line[field_start_positions[i]:field_start_positions[i+1]-1]
        result.append(elem_value)
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
for column_idx in range(len(table[0])):
    column_buffer = [] # holds a column of the original matrix
    for row_idx in range(len(table)):
        column_buffer.append(table[row_idx][column_idx])
    transposed.append(column_buffer)

first_colum = transposed[0]
op = first_colum[-1]

# Create number for each 'internal' colum, e.g. 356
def assemble_vertical_number(external_column, internal_column_idx):

    result = 0
    exponent = 0
    for row_idx, elem in enumerate(reversed(external_column)):
        digit=elem[internal_column_idx]
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

    for idx in range(len(col[0])):
        value = assemble_vertical_number(col[:-1], idx)
        accu = eval(f"accu {op} value")

    result += accu

print(int(result))
