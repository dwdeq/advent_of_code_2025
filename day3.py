import sys

banks = []

for bank in sys.stdin:
    banks.append(bank.rstrip())

# Part 1

finaljoltage = 0

for bank in banks:
    jolt1 = bank[0]
    idx1 = 0
    for idx in range(len(bank)-1):
        jolt = bank[idx]
        if jolt > jolt1:
            jolt1 = jolt
            idx1 = idx

    jolt2 = bank[idx+1]
    for idx in range(idx1+1,len(bank)):
        jolt = bank[idx]
        if jolt > jolt2:
            jolt2 = jolt

    finaljoltage += int(jolt1+jolt2)

print(finaljoltage)

# Part 2

finaljoltage = 0

numslist = []

for bank in banks:
    
    joltage = []

    for x in range(12):
        if x == 0:
            maxidx = 0
        else:
            maxidx = joltage[x-1][1] + 1
        maxnum = bank[maxidx]
        startidx = maxidx
        for idx in range(startidx, len(bank)-11+x):
            num = bank[idx]
            if num > maxnum:
                maxnum = num
                maxidx = idx
        joltage.append((maxnum, maxidx))     
    
    numslist.append(joltage)

for nums in numslist:
    finalnum = []
    for num,idx in nums:
        finalnum.append(num)
    finaljoltage += int(''.join(finalnum))

print(finaljoltage)