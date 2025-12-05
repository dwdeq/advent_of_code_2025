import sys

file = []

for line in sys.stdin:
    file.append(line.rstrip())

ranges = []
ids = []

idflag = True

for line in file:
    if line == "":
        idflag = False
        continue
    if idflag:
        newtup = tuple(line.split('-'))
        newtup = (int(newtup[0]),int(newtup[1]))
        ranges.append(newtup)
    else: 
        ids.append(int(line))

# Part 1

ids.sort()

count = 0

for id in ids:
    for start, end in ranges:
        if start <= id and end >= id:
            count += 1
            break

print(count)

# Part 2

'''
for start, end in ranges[1:]:
    flag = True
    for idx in range(len(database)):
        dstart = database[idx][0]
        dend = database[idx][1]
        if start <= dend and end >= dstart:
            database[idx] = (min(start,dstart),max(end,dend))
            flag = False
            break
    if flag: database.append((start,end))
'''

database = ranges.copy()

oldlen = len(database)+1

changed = True
while changed:
    changed = False
    for i in range(len(database)-1, -1, -1):
        start_i, end_i = database[i]

        for j in range(i-1, -1, -1):
            start_j, end_j = database[j]

            if start_i <= end_j and end_i >= start_j:
                # merge
                new_start = min(start_i, start_j)
                new_end   = max(end_i, end_j)

                database[i] = (new_start, new_end)
                database.pop(j)
                changed = True
                break

    
count = 0

for start, end in database:
    count += end - start + 1

print(count)