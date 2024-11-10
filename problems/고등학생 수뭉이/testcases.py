import random
import pathlib
import string

from oj import Problem

MAX_N = 100
TEST_COUNT = 10

DIR = pathlib.Path("/Users/kimjunhwan/Desktop/python codingtest/python/soomoongcup-2024-2/problems/고등학생 수뭉이")

problem = Problem(answer_file=DIR/"solution.py")

# 예제 1
with problem.testcase('1') as sys:
    N = 14
    sys.stdin.write('{N}\n'.format(N=N))
    S = "Hello, World! "
    sys.stdin.write(f'{S}\n')

# 예제 2
with problem.testcase('2') as sys:
    N = 174
    sys.stdin.write('{N}\n'.format(N=N))
    S = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation"
    sys.stdin.write(f'{S}\n')

# 최악의 경우
with problem.testcase('3') as sys:
    N = MAX_N
    sys.stdin.write('{N}\n'.format(N=N))
    S = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(N))
    sys.stdin.write(f'{S}\n')

# 랜덤 테스트 케이스
for i in range(4, TEST_COUNT + 1):
    with problem.testcase(str(i)) as sys:
        N = random.randint(1, MAX_N)
        sys.stdin.write('{N}\n'.format(N=N))
        S = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(N))
        sys.stdin.write(f'{S}\n')

problem.save(zipname=DIR/"high.zip", dirname=DIR/"testcase")