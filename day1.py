import sys

codes = sys.stdin

count = 0
idx = 50

for code in codes:
    code = code.rstrip()
    direct = code[0]
    amt = int(code[1:])
    if direct == 'L': amt *= -1
    idx += amt
    idx %= 100
    if idx == 0: count += 1

print(count)

count = 0
idx = 50

for code in codes:
    code = code.rstrip()
    direct = code[0]
    amt = int(code[1:])
    while amt != 0:
        if direct == 'R': idx += 1
        else:             idx -= 1
        idx %= 100
        amt -= 1
        if idx == 0: count += 1

print(count)