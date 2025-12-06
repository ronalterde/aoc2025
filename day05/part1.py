# Idea: put all fresh numbers into a set
import time

fresh_ranges = []
available_numbers = []

# with open('example.txt') as f:
with open('input.txt') as f:
    has_seen_empty_line = False
    for line in f:
        line = line.strip()
        if has_seen_empty_line:
            available_numbers.append(int(line))
        elif line == "":
            has_seen_empty_line = True
        else:
            parts = line.split('-')
            fresh_ranges.append((int(parts[0]), int(parts[1])))

print(fresh_ranges)

# for all ids, compare against all ranges
def is_in_range(id):
    for i in fresh_ranges:
        if id >= i[0] and id <= i[1]:
            return True
    return False

sum = 0
for i in available_numbers:
    # print(is_in_range(i))
    if is_in_range(i):
        sum += 1
print(sum)

###############
# Alternatiive solution: works for example but is way too slow for input.txt
###############
# fresh_ids = set()
# for i in fresh_ranges:
#     for k in range(i[0], i[1]+1):
#         fresh_ids.add(k)
#     time.sleep(100)
# intersection = fresh_ids.intersection(set(available_numbers))
# print(len(intersection))
