import sys


N, K = map(int, sys.stdin.readline().split())

A = []
for _ in range(N):
    name, a, b = sys.stdin.readline().split()
    A.append((int(a), name))
    A.append((int(b), name))

A.sort(key=lambda x: x[0])

sys.stdout.write(A[(K-1) % (2*N)][1]+'\n')
