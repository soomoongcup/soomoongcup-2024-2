import pathlib
import random

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
MAX_N = 10000


###############################################################
# 테스트케이스 생성
###############################################################

def testcases_for_accuracy(problem: Problem) -> None:
    # 정확성 테스트케이스 생성
    with problem.testcase("1") as sys:
        sys.stdin.write("7")

    ...


def testcases_for_efficiency(problem: Problem) -> None:
    # 효율성 테스트케이스 생성
    with problem.testcase("6") as sys:
        N = random.randint(MIN_N, MAX_N)
        sys.stdin.write(f"{N}")

    ...


###############################################################
# 생성한 테스트케이스 저장
###############################################################

problem = Problem(answer_file=SOLUTION_FILE)

testcases_for_accuracy(problem)
testcases_for_efficiency(problem)

problem.save(zipname=TESTCASE_ZIP_FILE, dirname=TESTCASE_DIR)
