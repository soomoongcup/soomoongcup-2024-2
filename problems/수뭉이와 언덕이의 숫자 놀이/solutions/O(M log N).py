import sys
import heapq


POP_MIN_HEAP = '-1'
POP_MAX_HEAP = '1'

max_heap = []
min_heap = []


def max_heap_pop() -> int:
    return -heapq.heappop(max_heap)


def max_heap_push(x: int) -> None:
    heapq.heappush(max_heap, -x)


def min_heap_pop() -> int:
    return heapq.heappop(min_heap)


def min_heap_push(x: int) -> None:
    heapq.heappush(min_heap, x)


def max_heap_top() -> int:
    return -max_heap[0]


def min_heap_top() -> int:
    return min_heap[0]


N = int(sys.stdin.readline())

for x in map(int, sys.stdin.readline().split()):
    min_heap_push(x)

for x in map(int, sys.stdin.readline().split()):
    max_heap_push(x)


M = int(sys.stdin.readline())

for i in range(M):
    if POP_MIN_HEAP == sys.stdin.readline().strip():
        max_heap_push(min_heap_pop())
    else:
        min_heap_push(max_heap_pop())

if abs(min_heap_top()) <= abs(max_heap_top()):
    print(min_heap_top())
else:
    print(max_heap_top())
