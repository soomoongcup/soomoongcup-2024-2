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
MAX_N = 100*1000

MIN_M = 1
MAX_M = 20_001_000

MIN_SET = 0
MAX_SET = int(1e6)

MIN_ADD = 0
MAX_ADD = int(1e6)

MIN_PRN = 0
MAX_PRN = int(1e3)

MIN_CNT = 0
MAX_CNT = int(1e3)

OPERATIONS = ["SET", "ADD", "PRN", "CNT"]


def random_operation(w_set: int, w_add: int, w_prn: int, w_cnt: int) -> str:
    m = w_set + w_add + w_prn + w_cnt
    return random.choices(OPERATIONS, weights=[w_set/m, w_add/m, w_prn/m, w_cnt/m], k=1)[0]


def random_x(N: int) -> int:
    return random.randint(1, N)


def random_y() -> int:
    return random.randint(0, 4)


def random_z() -> int:
    return random.randint(-4, 4)


def random_k_uniques(k: int, lo: int, hi: int) -> typing.List[int]:
    return random.sample(range(lo, hi+1), k)


def random_testcase(N: int, M: int, op_set: int, op_add: int, op_prn: int, op_cnt: int, skip_first_line=False) -> typing.List[str]:
    assert MIN_N <= N <= MAX_N
    assert MIN_M <= M <= MAX_M
    assert MIN_SET <= op_set <= MAX_SET
    assert MIN_ADD <= op_add <= MAX_ADD
    assert MIN_PRN <= op_prn <= MAX_PRN
    assert MIN_CNT <= op_cnt <= MAX_CNT
    lines = []
    if not skip_first_line:
        lines.append(f"{N} {M}\n")
    for _ in range(op_set+op_add+op_prn+op_cnt):
        op = random_operation(op_set, op_add, op_prn, op_cnt)
        match op:
            case "SET":
                x = random_x(N)
                y = random_y()
                lines.append(f"SET {x} {y}\n")
                op_set -= 1
            case "ADD":
                y = random_y()
                z = random_z()
                lines.append(f"ADD {y} {z}\n")
                op_add -= 1
            case "PRN":
                x = random_x(N)
                lines.append(f"PRN {x}\n")
                op_prn -= 1
            case "CNT":
                y = random_y()
                lines.append(f"CNT {y}\n")
                op_cnt -= 1
    return lines


###############################################################
# 테스트케이스 생성
###############################################################

def testcases_for_accuracy(problem: Problem) -> None:
    # 정확성 테스트케이스 생성
    with problem.testcase("1") as sys:
        # 예제 테스트케이스
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

    with problem.testcase("2") as sys:
        # "ADD 0 음수" 일때의 처리를 검사하는 테케.
        sys.stdin.write("100 7\n")
        sys.stdin.write("SET 2 2\n")
        sys.stdin.write("SET 3 2\n")
        sys.stdin.write("CNT 2\n")
        sys.stdin.write("ADD 2 -2\n")
        sys.stdin.write("CNT 0\n")
        sys.stdin.write("ADD 0 -4\n")
        sys.stdin.write("CNT 0\n")

    for i in range(3, 6):
        with problem.testcase(str(i)) as sys:
            op_set = random.randint(MIN_SET, 50)
            op_add = random.randint(MIN_ADD, 50)
            op_cnt = random.randint(MIN_CNT, 50)
            op_prn = random.randint(MIN_PRN, 50)
            N = random.randint(MIN_N, MAX_N)
            M = op_set + op_add + op_cnt + op_prn
            lines = random_testcase(N, M, op_set, op_add, op_prn, op_cnt)
            sys.stdin.writelines(lines)


def testcases_for_efficiency(problem: Problem) -> None:
    # 효율성 테스트케이스 생성

    with problem.testcase("6") as sys:
        print(f"SET이 최악인 경우. SET={MAX_SET:,}")
        op_set = MAX_SET
        op_add = 1
        op_cnt = 1
        op_prn = 1
        N = MAX_N
        M = op_set + op_add + op_cnt + op_prn
        lines = random_testcase(N, M, 0, op_add, op_prn, op_cnt)
        sys.stdin.writelines(lines)
        lines = random_testcase(N, M, op_set, 0, 0, 0, skip_first_line=True)
        sys.stdin.writelines(lines)

    with problem.testcase("7") as sys:
        print(f"ADD가 최악인 경우. ADD={MAX_ADD:,}")
        op_set = 1
        op_add = MAX_ADD
        op_cnt = 1
        op_prn = 1
        N = MAX_N
        M = op_set + op_add + op_cnt + op_prn
        lines = random_testcase(N, M, op_set, 0, op_prn, op_cnt)
        sys.stdin.writelines(lines)
        lines = random_testcase(N, M, 0, op_add, 0, 0, skip_first_line=True)
        sys.stdin.writelines(lines)

    with problem.testcase("8") as sys:
        print(f"CNT가 최악인 경우. CNT={MAX_CNT:,}")
        op_set = 1
        op_add = 1
        op_cnt = MAX_CNT
        op_prn = 1
        N = MAX_N
        M = op_set + op_add + op_cnt + op_prn
        lines = random_testcase(N, M, op_set, op_add, op_cnt, 0)
        sys.stdin.writelines(lines)
        lines = random_testcase(N, M, 0, 0, 0, op_cnt, skip_first_line=True)
        sys.stdin.writelines(lines)

    with problem.testcase("9") as sys:
        print(f"PRN가 최악인 경우. PRN={MAX_PRN:,}")
        op_set = 1
        op_add = 1
        op_cnt = 1
        op_prn = MAX_PRN
        N = MAX_N
        M = op_set + op_add + op_cnt + op_prn
        lines = random_testcase(N, M, op_set, op_add, 0, op_cnt)
        sys.stdin.writelines(lines)
        lines = random_testcase(N, M, 0, 0, op_prn, 0, skip_first_line=True)
        sys.stdin.writelines(lines)

    with problem.testcase("10") as sys:
        print("모든 값이 최악인 경우")
        op_set = MAX_SET
        op_add = MAX_ADD
        op_cnt = MAX_CNT
        op_prn = MAX_PRN
        N = random.randint(MIN_N, MAX_N)
        M = op_set + op_add + op_cnt + op_prn
        lines = random_testcase(N, M, op_set, op_add, op_prn, op_cnt)
        sys.stdin.writelines(lines)


###############################################################
# 생성한 테스트케이스 저장
###############################################################
problem = Problem(answer_file=SOLUTION_FILE)

testcases_for_accuracy(problem)
testcases_for_efficiency(problem)

problem.save(zipname=TESTCASE_ZIP_FILE, dirname=TESTCASE_DIR)
