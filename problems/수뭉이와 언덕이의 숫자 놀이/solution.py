import heapq
import sys
input = sys.stdin.readline

N = int(input())

soomoong = list(map(int, input().split()))
unduck = list(map(int, input().split()))
unduck = [-x for x in unduck] # O(N)

heapq.heapify(soomoong) # O(NlogN)
heapq.heapify(unduck) # O(NlogN)

M = int(input())

for i in range(M): # O(M * logN)
    temp = int(input())
    if temp == -1:
        heapq.heappush(unduck, -heapq.heappop(soomoong))
    elif temp == 1:
        heapq.heappush(soomoong, -heapq.heappop(unduck))

abs_min = heapq.heappop(soomoong)
abs_max = heapq.heappop(unduck)

if abs(abs_min) <= abs(abs_max):
    print(abs_min)
else:
    print(abs_max)