# You'll need to find the largest possible joltage each bank can produce. In the above example:
#
#     In 987654321111111, you can make the largest joltage possible, 98, by turning on the first two batteries.
#     In 811111111111119, you can make the largest joltage possible by turning on the batteries labeled 8 and 9, producing 89 jolts.
#     In 234234234234278, you can make 78 by turning on the last two batteries (marked 7 and 8).
#     In 818181911112111, the largest joltage you can produce is 92.

with open('example.txt') as f:
# with open('input.txt') as f:
    banks = f.readlines()

def get_max(bank):
    '''
    Return max and its index
    '''
    sorted_bank = sorted([(int(k), i) for i, k in enumerate(bank)])
    return sorted_bank[-1]

joltages = []

for bank in banks:
    bank = bank.strip()

    # Take the one with the largest value
    largest_battery = get_max(bank)

    # Find the second-largest one
    if largest_battery[1] < (len(bank) - 1):
        # If the max is *not* at the rightmost position,
        # look at values on the right side
        right_side = bank[largest_battery[1]+1:]
        joltages.append(int(str(largest_battery[0]) + str(get_max(right_side)[0])))
    else:
        # If the max is at the rightmost position,
        # look at values on the left side
        left_side = bank[:largest_battery[1]]
        joltages.append(int(str(get_max(left_side)[0]) + str(largest_battery[0])))


print(sum(joltages))

