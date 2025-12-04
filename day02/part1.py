# Since the young Elf was just doing silly patterns, you can find the invalid IDs by looking for any ID which is made only of some sequence of digits repeated twice. So, 55 (5 twice), 6464 (64 twice), and 123123 (123 twice) would all be invalid IDs.

# Example:
# - 11-22 has two invalid IDs, 11 and 22.
# - 95-115 has one invalid ID, 99.
# - 998-1012 has one invalid ID, 1010.
# - 1188511880-1188511890 has one invalid ID, 1188511885.
# - 222220-222224 has one invalid ID, 222222.
# - 1698522-1698528 contains no invalid IDs.
# - 446443-446449 has one invalid ID, 446446.
# - 38593856-38593862 has one invalid ID, 38593859.
# - The rest of the ranges contain no invalid IDs.

with open('input.txt') as f:
    l = f.readline()

ll = l.strip().split(',')
lll = [i.split('-') for i in ll]
llll = [(int(i[0]), int(i[1])) for i in lll]

def is_invalid_id(a):
    return a[:int(len(a)/2)] == a[int(len(a)/2):]

result = 0
for i in llll:
    for k in range(i[0], i[1]+1):
        if is_invalid_id(str(k)):
            result += k

print(result)

