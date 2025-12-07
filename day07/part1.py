import argparse
# Idea: Merge current line into next, resolving splits by search-and-replace

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", required=True, help="Path to the input file")
args = parser.parse_args()

lines_converted = []
with open(args.input) as f:
    for line in f:
        # Introduce new encoding so we can use regular math operators:
        # . -> 0
        # | -> 2
        # ^ -> 4
        # S -> 8
        line_converted_to_numbers = line.strip().replace('.', '0').replace('|', '2').replace('^', '4').replace('S', '8')
        line_as_list = [int(i) for i in line_converted_to_numbers]
        lines_converted.append(line_as_list)

def merge(current_line, next_line):
    '''Merging: add previous line to current, pointwise'''
    merged_line = []
    for i, _ in enumerate(current_line):
        merged_line.append(current_line[i] + next_line[i])
    return merged_line

def apply_post_merge_rules(line_buffer):
    global split_count

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

split_count = 0
line_buffer = lines_converted[0]
for i, _ in enumerate(lines_converted[1:-1]):
    line_buffer = merge(line_buffer, lines_converted[i+1])
    apply_post_merge_rules(line_buffer)
    print(str(line_buffer).replace('2', '|'))

print('==== split count (the puzzle solution):', split_count)

