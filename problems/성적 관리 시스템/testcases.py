import pathlib
import random

# 이 파일과 동일한 폴더에 oj.py가 있어야 합니다.
# oj.py 주소: https://gist.github.com/hepheir/c4c6326c48b1af344196c1d115d4eca1

from oj import Problem


BASE_DIR = pathlib.Path(__file__).parent.resolve()

SOLUTION_FILE = BASE_DIR/"solution.py"
TESTCASE_DIR = BASE_DIR/"testcase"
TESTCASE_ZIP_FILE = BASE_DIR/"grades.zip"


###############################################################
# 문제 생성과 관련된 상수, 유틸리티 함수 정의
###############################################################

MIN_N = int(1e5)
MAX_M = int(20002000)

MIN_SET = 1
MAX_SET = int(1e7)

MIN_ADD = 1
MAX_ADD = int(1e7)

MIN_PRN = 1
MAX_PRN = int(1e3)

MIN_CNT = 1
MAX_CNT = int(1e3)


###############################################################
# 테스트케이스 생성
###############################################################

problem = Problem(answer_file=SOLUTION_FILE)


# 예제 테스트케이스 생성

with problem.testcase("1") as sys:
    inst = [
        "SET 1 2",
        "PRN 1",
        "SET 2 2",
        "PRN 2",
        "ADD 2 2",
        "SET 1 1",
        "PRN 1",
        "CNT 2",
        "PRN 3",
    ]
    N = 3
    M = len(inst)
    sys.stdin.write(f"{N} {M}\n")
    sys.stdin.write("\n".join(inst))


# 랜덤 테스트케이스 생성


# 생성한 테스트케이스 저장

problem.save(zipname=TESTCASE_ZIP_FILE, dirname=TESTCASE_DIR)
