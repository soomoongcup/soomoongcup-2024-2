import random
import pathlib

from oj import Problem

# 모범 풀이 시간 복잡도 10N
# 목표 시간 복잡도 O(N)
# 파이썬 1초당 40,000,000이라고 계산
# N = 4,000,000

MAX_N = 40 * 10000
MAX_A = 100 * 10000
TEST_COUNT = 1 + 3

DIR = pathlib.Path("/Users/kimjunhwan/Desktop/python codingtest/python/soomoongcup-2024-2/problems/수뭉이의 꿈")

problem = Problem(answer_file=DIR/"solution.py")

# 완전 탐색 (시간 복잡도 O(N!))
## 예제 1
with problem.testcase('1') as sys:
    N = 3
    sys.stdin.write('{N}\n'.format(N=N))
    sys.stdin.write('1 2 3 4 5\n')
    sys.stdin.write('2 3 4 5 6\n')
    sys.stdin.write('4 5 6 7 8\n')

## 예제 2
with problem.testcase('2') as sys:
    N = 4
    sys.stdin.write('{N}\n'.format(N=N))
    sys.stdin.write('1 2 3 4 5\n')
    sys.stdin.write('6 7 8 9 10\n')
    sys.stdin.write('3 11 12 13 14\n')
    sys.stdin.write('11 15 16 17 18\n')

## 10 이하
for i in range(3, 4 + 1):
    with problem.testcase(i) as sys:
        N = i + 2
        sys.stdin.write('{N}\n'.format(N=N))
        for _ in range(N):
            sys.stdin.write('{A} {B} {C} {D} {E}\n'.format(A=random.randint(1, MAX_A), B=random.randint(1, MAX_A), C=random.randint(1, MAX_A), D=random.randint(1, MAX_A), E=random.randint(1, MAX_A)))

# 10
with problem.testcase('5') as sys:
        N = 10
        sys.stdin.write('{N}\n'.format(N=N))
        for _ in range(N):
            sys.stdin.write('{A} {B} {C} {D} {E}\n'.format(A=random.randint(1, MAX_A), B=random.randint(1, MAX_A), C=random.randint(1, MAX_A), D=random.randint(1, MAX_A), E=random.randint(1, MAX_A)))


# 그리디 (시간 복잡도 O(N))
## 12 (최소)
with problem.testcase('6') as sys:
    N = 12
    sys.stdin.write('{N}\n'.format(N=N))
    for _ in range(N):
        sys.stdin.write('{A} {B} {C} {D} {E}\n'.format(A=random.randint(1, MAX_A), B=random.randint(1, MAX_A), C=random.randint(1, MAX_A), D=random.randint(1, MAX_A), E=random.randint(1, MAX_A)))

## 1000
with problem.testcase('7') as sys:
    N = 1000
    sys.stdin.write('{N}\n'.format(N=N))
    for _ in range(N):
        sys.stdin.write('{A} {B} {C} {D} {E}\n'.format(A=random.randint(1, MAX_A), B=random.randint(1, MAX_A), C=random.randint(1, MAX_A), D=random.randint(1, MAX_A), E=random.randint(1, MAX_A)))

## 10000 ~ 최악 전
for i in range(8, 9 + 1):
    with problem.testcase(i) as sys:
        N = random.randint(10000, MAX_N)
        sys.stdin.write('{N}\n'.format(N=N))
        for _ in range(N):
            sys.stdin.write('{A} {B} {C} {D} {E}\n'.format(A=random.randint(1, MAX_A), B=random.randint(1, MAX_A), C=random.randint(1, MAX_A), D=random.randint(1, MAX_A), E=random.randint(1, MAX_A)))

## 최악의 경우
with problem.testcase('10') as sys:
    N = MAX_N
    sys.stdin.write('{N}\n'.format(N=N))
    for _ in range(N):
        sys.stdin.write('{A} {B} {C} {D} {E}\n'.format(A=random.randint(1, MAX_A), B=random.randint(1, MAX_A), C=random.randint(1, MAX_A), D=random.randint(1, MAX_A), E=random.randint(1, MAX_A)))

problem.save(zipname=DIR/"dream.zip", dirname=DIR/"testcase")