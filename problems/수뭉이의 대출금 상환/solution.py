# 테케 생성 코드 발췌

import sys

def custom_round(x):
    # 0.5 이상일 경우 올림, 미만일 경우 내림
    if x - int(x) >= 0.5:
        return int(x) + 1
    return int(x)

T = int(sys.stdin.readline())
for _ in range(T):
    R, B, M = map(float, sys.stdin.readline().split())
    months = 0
    debt = B
    initial_debt = B

    while debt > 0:
        months += 1
        if months > 1200:
            sys.stdout.write("impossible\n")
            break

        # 매월 초 이자 계산 (원 단위 반올림)
        interest = custom_round(debt * R / 100)
        debt += interest

        # 매월 말 상환
        debt -= M
        debt = custom_round(debt)

        if debt >= initial_debt:
            sys.stdout.write("impossible\n")
            break
    else:
        sys.stdout.write(f"{months}\n")
