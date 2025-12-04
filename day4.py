import sys

grid = []

for line in sys.stdin:
    grid.append(list(line.rstrip()))

# Part 1

count = 0

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '@':
            adjcount = 0
            for k in range(-1,2,1):
                for l in range (-1,2,1):
                    if i+k >= 0 and i+k < len(grid):
                        if j+l >= 0 and j+l < len(grid[i]):
                            adjcount += (grid[i+k][j+l] == '@')
            if adjcount <= 4:
                count += 1

print(count)

# Part 2

lidx = -1
count = 0
prevcount = -1

while prevcount != count:
    lidx += 1
    prevcount = count
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '@':
                adjcount = 0
                for k in range(-1,2,1):
                    for l in range (-1,2,1):
                        if i+k >= 0 and i+k < len(grid):
                            if j+l >= 0 and j+l < len(grid[i]):
                                adjcount += (grid[i+k][j+l] == '@' or grid[i+k][j+l] == 'x')
                if adjcount <= 4:
                    grid[i][j] = 'x'

    xcount = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'x':
                xcount += 1
                grid[i][j] = '.'

    
    count += xcount

    print(f'loop {lidx}: {xcount} x\'s')

print(count)