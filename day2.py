import sys
import time

ids = sys.stdin

for id in ids:
    idlist = id.split(',')

# Part 1

badids = []

for idxs in idlist:
    start,end = idxs.split('-')
    for id in range(int(start),int(end)+1):
        id = str(id)
        if id[:len(id)//2] == id[len(id)//2:]:
            badids.append(int(id))

sum = 0
for badid in badids:
    sum += badid
print(sum,'\n')

# Part 2

def checkrep(num, kmer):
    for i in range(0,len(num),len(kmer)):
        if num[i:i+len(kmer)] != kmer: return False
    return True

badids = []

t0 = time.time()

for idxs in idlist:
    start,end = idxs.split('-')
    for id in range(int(start),int(end)+1):
        id = str(id)
        for n in range(len(id)//2):
            m = len(id)//2 - n
            if id[:m] == id[-m:]:
                if checkrep(id, id[:m]): 
                    badids.append(int(id))

t1 = time.time()

badids = list(set(badids))

t2 = time.time()

sum = 0
for badid in badids:
    sum += badid

t3 = time.time()

print(f'{sum} \nlooped algorithm: {t1-t0} \nremoving duplicates: {t2-t1} \ncalculating final value: {t3-t2}')