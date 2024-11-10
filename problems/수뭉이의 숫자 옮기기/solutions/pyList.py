import sys
input = sys.stdin.readline
N, M = map(int, input().split())
numbers = list(range(1, N+1))
for _ in range(M):
    A, B, C = map(int, input().split())
    cut = numbers[A-1:B]
    numbers[A-1:B] = []
    numbers[C:C] = cut
# 전체 출력
for num in numbers:
    print(num)