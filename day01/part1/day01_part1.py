import re

with open('input.txt') as f:
    l = f.readlines()

dial_moves = []
for s in l:
    m = re.match(r"([A-Za-z]+)(\d+)", s)
    sign = -1 if m.groups()[0] == "L" else 1
    number = int(m.groups()[1])
    dial_moves.append((sign * number))

INIT = 50

result_sequence = []
accu = INIT
for i in dial_moves:
    accu = (accu + i) % 100
    result_sequence.append(accu)
# print(result_sequence)

print(result_sequence.count(0))


