# Now, an ID is invalid if it is made only of some sequence of digits repeated at least twice. So, 12341234 (1234 two times), 123123123 (123 three times), 1212121212 (12 five times), and 1111111 (1 seven times) are all invalid IDs.

# Example:
# - 11-22 still has two invalid IDs, 11 and 22.
# - 95-115 now has two invalid IDs, 99 and 111.
# - 998-1012 now has two invalid IDs, 999 and 1010.
# - 1188511880-1188511890 still has one invalid ID, 1188511885.
# - 222220-222224 still has one invalid ID, 222222.
# - 1698522-1698528 still contains no invalid IDs.
# - 446443-446449 still has one invalid ID, 446446.
# - 38593856-38593862 still has one invalid ID, 38593859.
# - 565653-565659 now has one invalid ID, 565656.
# - 824824821-824824827 now has one invalid ID, 824824824.
# - 2121212118-2121212124 now has one invalid ID, 2121212121.

# Adding up all the invalid IDs in this example produces 4174379265.

# steps are prime factors! No, not exactly - just divisors!

with open('input.txt') as f:
    l = f.readline()

ll = l.strip().split(',')
lll = [i.split('-') for i in ll]
llll = [(int(i[0]), int(i[1])) for i in lll]

def find_divisors(n):
  divisors = []
  for i in range(1, n + 1):
    if n % i == 0:
      divisors.append(i)
  return divisors

def is_invalid_id(a):
    for x in find_divisors(len(a)):
        parts = [a[i:i+x] for i in range(0, len(a), x)]
        all_parts_equal = all(x==parts[0] for x in parts) and len(parts) > 1
        if all_parts_equal:
            return True
    return False

result = 0
for i in llll:
    for k in range(i[0], i[1]+1):
        if is_invalid_id(str(k)):
            result += k

print(result)

