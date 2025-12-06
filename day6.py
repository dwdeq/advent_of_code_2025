import sys

file = []

for line in sys.stdin:
    file.append(line.rstrip())

# Part 1

for idx in range(len(file)):
    file[idx] = file[idx].split()

total = 0

for probidx in range(len(file[0])):

    probresult = int(file[0][probidx])
    symbol = file[4][probidx]

    for numidx in range(1,len(file)-1):
        num = int(file[numidx][probidx])

        if symbol == '*':
            probresult *= num
        elif symbol == '+':
            probresult += num
        else:
            print("whoops")
    
    total += probresult

print(total)

# Part 2

total = 0

end = -1
start = len(file[4])

for idx in range(len(file[4])-1,-1,-1):

    operator = file[4][idx]

    probresult = 0
    if operator == '*':
        probresult = 1
    
    if operator == ' ':
        continue
        
    end = idx
    
    for numidx in range(start,end-1,-1):
        number = ''

        for digitidx in range(4):
            digit = file[digitidx][numidx]

            if digit != ' ':
                number += digit

        number = int(number)
        
        if operator == '*':
            probresult *= number
        elif operator == '+':
            probresult += number
        else:
            print("whoops")

    total += probresult
    start = idx - 2

print(total)


