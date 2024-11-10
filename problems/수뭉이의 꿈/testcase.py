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

DIR = pathlib.Path("/Users/kimjunhwan/Desktop/python codingtest/soomoongcup-2024-2/problems/soomoong-dream/")

problem = Problem(answer_file=DIR/"solution.py")

# 최악의 경우
with problem.testcase('1') as sys:
    N = MAX_N
    sys.stdin.write('{N}\n'.format(N=N))
    for _ in range(N):
        sys.stdin.write('{A} {B} {C} {D} {E}\n'.format(A=random.randint(1, MAX_A), B=random.randint(1, MAX_A), C=random.randint(1, MAX_A), D=random.randint(1, MAX_A), E=random.randint(1, MAX_A)))

# 그리디만 목표고 OJ룰이기 때문에 최대한 최악에 가깝게 테스트케이스 선정
for i in range(2, TEST_COUNT + 1):
    with problem.testcase(i) as sys:
        N = random.randint(MAX_N - 10, MAX_N)
        sys.stdin.write('{N}\n'.format(N=N))
        for _ in range(N):
            sys.stdin.write('{A} {B} {C} {D} {E}\n'.format(A=random.randint(1, MAX_A), B=random.randint(1, MAX_A), C=random.randint(1, MAX_A), D=random.randint(1, MAX_A), E=random.randint(1, MAX_A)))

problem.save(zipname=DIR/"dream.zip", dirname=DIR/"testcase")