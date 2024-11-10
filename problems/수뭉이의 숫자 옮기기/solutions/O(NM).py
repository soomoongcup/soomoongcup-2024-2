import sys


N, M = map(int, sys.stdin.readline().split())

curr = [*range(N+1)]
# O(MN)
for m in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    prev = curr
    cut = prev[A:B+1]
    curr = prev[:A] + prev[B+1:] # O(N)
    curr = curr[:C+1] + cut + curr[C+1:] # O(N)

for i in range(1, N+1):
    print(curr[i])
