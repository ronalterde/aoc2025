import re

# with open('input.txt') as f:
with open('example.txt') as f:
    l = f.readlines()

dial_moves = []
for s in l:
    m = re.match(r"([A-Za-z]+)(\d+)", s)
    sign = -1 if m.groups()[0] == "L" else 1
    number = int(m.groups()[1])
    dial_moves.append((sign * number))
# print(dial_moves)

INIT = 50

result_sequence = []
accu = INIT
additionals = 0

for i in dial_moves:
    print(accu, i, (accu + i) % 100, (accu + i))
    result_sequence.append(accu)
    if (accu + i) < 0:
        additionals = additionals + abs(int((accu+i)/100)) + 1
    elif accu == 0:
        pass
    else:
        additionals = additionals + int((accu+i)/100)
    accu = (accu + i) % 100

print("result:", result_sequence.count(0))
print("additionals:", additionals)

