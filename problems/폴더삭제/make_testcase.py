# 구해야 하는 것 : 첫번째 줄  -> N행, M 열 이는 (1<=  <= 50)임
                # 두번째 줄부터 -> N+1번째 줄까지 '.' 또는 'D'

from random import randrange
from random import randint
import random

class Calculate:
    def __init__(self, n): # 생성자
        self.n = n
    
    def values(self):
        res = []
        N = randint(1, 50) # 1 ~ 50 여야함
        M = randrange(1, 51) # 1 ~ 50 여야함        
        res.append([N, M])

        D_or_Jum = ['D', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X','X', 'X', 'X'] # D가 나올 확률 1/15
        for _ in range(N): # N행 M열 만큼 반복
            str = ''
            for _ in range(M):
                random_output = random.choice(D_or_Jum)
                str += random_output
            res.append(str)
        return res
