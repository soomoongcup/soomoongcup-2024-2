import random
import pathlib
import string

from oj import Problem

random.seed("high")
MAX_N = 10000
TEST_COUNT = 100
korean_characters = ''.join(chr(i) for i in range(0xAC00, 0xD7A4))

DIR = pathlib.Path("/Users/kimjunhwan/Desktop/python codingtest/soomoongcup-2024-2/problems/high/")

problem = Problem(answer_file=DIR/"solution.py")

with problem.testcase('1') as sys:
    N = MAX_N
    sys.stdin.write('{N}\n'.format(N=N))
    S = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(N))
    sys.stdin.write(f'{S}\n')

for i in range(2, TEST_COUNT + 1):
    with problem.testcase(str(i)) as sys:
        N = random.randint(1, MAX_N)
        sys.stdin.write('{N}\n'.format(N=N))
        S = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(N))
        sys.stdin.write(f'{S}\n')

problem.save(zipname=DIR/"high.zip", dirname=DIR/"testcase")