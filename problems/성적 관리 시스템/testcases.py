import pathlib
import random
import typing

# 이 파일과 동일한 폴더에 oj.py가 있어야 합니다.
# oj.py 주소: https://gist.github.com/hepheir/c4c6326c48b1af344196c1d115d4eca1

from oj import Problem


BASE_DIR = pathlib.Path(__file__).parent.resolve()

SOLUTION_FILE = BASE_DIR/"solution.py"
TESTCASE_DIR = BASE_DIR/"testcase"
TESTCASE_ZIP_FILE = BASE_DIR/"testcase.zip"


# random 모듈의 함수들로 생성되는 값이 일관성을 갖도록 시드 설정
random.seed(0)

###############################################################
# 문제 생성과 관련된 상수, 유틸리티 함수 정의
# (예: N의 최댓값, 최솟값 정의 등)
###############################################################

MIN_N = 1
MAX_N = 100000

MIN_M = 1
MAX_M = 20002000

MIN_SET = 1
MAX_SET = int(1e7)

MIN_ADD = 1
MAX_ADD = int(1e7)

MIN_PRN = 1
MAX_PRN = int(1e3)

MIN_CNT = 1
MAX_CNT = int(1e3)

OPERATIONS = ["SET", "ADD", "PRN", "CNT"]


def random_operation() -> str:
    return random.choice(OPERATIONS)


def random_x(N: int) -> int:
    return random.randint(1, N)


def random_y() -> int:
    return random.randint(0, 4)


def random_z() -> int:
    return random.randint(-4, 4)


###############################################################
# 테스트케이스 생성
###############################################################

def testcases_for_accuracy(problem: Problem) -> None:
    # 정확성 테스트케이스 생성
    with problem.testcase("1") as sys:
        N = 3
        M = 9
        sys.stdin.write(f"{N} {M}\n")
        sys.stdin.write("SET 1 2\n")
        sys.stdin.write("PRN 1\n")
        sys.stdin.write("SET 2 2\n")
        sys.stdin.write("PRN 2\n")
        sys.stdin.write("ADD 2 2\n")
        sys.stdin.write("SET 1 1\n")
        sys.stdin.write("PRN 1\n")
        sys.stdin.write("CNT 2\n")
        sys.stdin.write("PRN 3\n")


def testcases_for_efficiency(problem: Problem) -> None:
    # 효율성 테스트케이스 생성
    for i in range(6, 10):
        with problem.testcase(str(i)) as sys:
            N = random.randint(MIN_N, MAX_N)
            M = 1000
            sys.stdin.write(f"{N} {M}\n")
            for i in range(M):
                op = random_operation()
                match op:
                    case "SET":
                        x = random_x(N)
                        y = random_y()
                        sys.stdin.write(f"{op} {x} {y}\n")
                    case "ADD":
                        y = random_y()
                        z = random_z()
                        sys.stdin.write(f"{op} {y} {z}\n")
                    case "PRN":
                        x = random_x(N)
                        sys.stdin.write(f"{op} {x}\n")
                    case "CNT":
                        y = random_y()
                        sys.stdin.write(f"{op} {y}\n")
    with problem.testcase("10") as sys:
        N = MAX_N
        M = 1000
        sys.stdin.write(f"{N} {M}\n")
        for i in range(M):
            op = random_operation()
            match op:
                case "SET":
                    x = random_x(N)
                    y = random_y()
                    sys.stdin.write(f"{op} {x} {y}\n")
                case "ADD":
                    y = random_y()
                    z = random_z()
                    sys.stdin.write(f"{op} {y} {z}\n")
                case "PRN":
                    x = random_x(N)
                    sys.stdin.write(f"{op} {x}\n")
                case "CNT":
                    y = random_y()
                    sys.stdin.write(f"{op} {y}\n")

###############################################################
# 생성한 테스트케이스 저장
###############################################################
problem = Problem(answer_file=SOLUTION_FILE)

testcases_for_accuracy(problem)
testcases_for_efficiency(problem)

problem.save(zipname=TESTCASE_ZIP_FILE, dirname=TESTCASE_DIR)
