import sys


n = int(input())
nlist = [False for _ in range(1_000_001)]

count = 0
for i in range(n):
    a, b, c, d, e = map(int, sys.stdin.readline().rstrip().split(' '))
    if(not ((nlist[a]) or (nlist[b]) or (nlist[c]) or (nlist[d]) or (nlist[e]))):
        count += 1
    nlist[a] = nlist[b] = nlist[c] = nlist[d] = nlist[e] = True

    
print(count)