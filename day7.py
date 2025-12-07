import sys

file = []

for line in sys.stdin:
    file.append(list(line.rstrip()))

startidx = -1

for idx in range(len(file[0])):
    if file[0][idx] == 'S':
        startidx = idx
        break

# Part 1

count = 0

manifold = file.copy()

idxs = [startidx]

for row in range(len(manifold)):
    newidxs = []
    for col in range(len(manifold[0])):
        if col in idxs and manifold[row][col] == '^':
            newidxs.append(col-1)
            newidxs.append(col+1)
            count += 1
        elif col in idxs:
            newidxs.append(col)
        else:
            continue
    idxs = newidxs

print(count)

# Part 2

count = 1

manifold = file.copy()

idxs = {}
idxs[startidx] = 1

for row in range(len(manifold)):
    newidxs = {}

    for col in range(len(manifold[0])):
        if col in idxs.keys() and manifold[row][col] == '^':

            if col-1 not in newidxs.keys():
                newidxs[col-1] = 0
            newidxs[col-1] += idxs[col]

            if col+1 not in newidxs.keys():
                newidxs[col+1] = 0
            newidxs[col+1] += idxs[col]

            count += idxs[col]

        elif col in idxs.keys():

            if col not in newidxs.keys():
                newidxs[col] = 0
            newidxs[col] += idxs[col]

        else:
            continue

    idxs = newidxs

    print(count)