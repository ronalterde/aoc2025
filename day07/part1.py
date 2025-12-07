# Idea: Merge current line into next, resolving splits by search-and-replace

# Introduce new encoding:
# . -> 0
# | -> 2
# ^ -> 4
# S -> 8

def merge(current_line, next_line):
    '''Merging: add previous line to current, pointwise'''
    merged_line = []
    for i, _ in enumerate(current_line):
        merged_line.append(current_line[i] + next_line[i])

    return merged_line

lines_converted = []
with open('example.txt') as f:
# with open('input.txt') as f:
    for line in f:
        line_converted_to_numbers = line.strip().replace('.', '0').replace('|', '2').replace('^', '4').replace('S', '8')
        line_as_list = [int(i) for i in line_converted_to_numbers]
        lines_converted.append(line_as_list)

merged_line = list(merge(lines_converted[0], lines_converted[1]))

split_count = 0

line_buffer = lines_converted[0]
for i, line in enumerate(lines_converted[1:-1]):
    line_buffer = merge(line_buffer, lines_converted[i+1])

    # Post-merge rules:
    # 8+0=8 -> 020 (relevant for start only)
    # 8+4=12 -> 242 (relevant for start only)
    # 2+4=6 -> 202 (splitter gets removed already for next operation)
    for i, _ in enumerate(line_buffer):
        if line_buffer[i] == 8:
            line_buffer[i] = 2
        elif line_buffer[i] == 12:
            line_buffer[i-1] = 2
            line_buffer[i] = 0
            line_buffer[i+1] = 2
        elif line_buffer[i] == 6:
            split_count += 1
            line_buffer[i-1] = 2
            line_buffer[i] = 0
            line_buffer[i+1] = 2

    print(str(line_buffer).replace('2', '|'))

print('split count:', split_count)


