# 구해야 하는 것 : 왼쪽 하단 모서리의 x1, y1 // 오른쪽 상단 모서리의 x2, y2
# 문제 조건 : 1~10 중 n개 만큼의 모서리 2개의 값이 필요함. (좌표 값은 1~100)임
# x, y 값은 각 100까지임

# 최악의 경우 : 10개의 사각형의 넓이가 모두 100인 경우 -> n^2 * 10 = n^2 => 100'00 * 10 = 100,000
# 1초, 메모리 아껴도 ok 32 mb

from random import randint

class Calculate:
    def __init__(self, n): # 생성자
        self.n = n
    
    def values(self):
        res = []
        for _ in range(self.n):
            # print(self.n)
            x1 = randint(0, 30000) # 0 ~ 30,000 여야함
            while(True):
                y1 = randint(0, 30000) # 0 ~ 30,000 여야함
                if x1 != y1: break

            while(True):
                x2 = randint(1, 30000) # 1 ~ 30000 까지 가능해야함
                y2 = randint(1, 30000) # 1 ~ 30000
                if x2 - x1 < 1 or y2 - y1 < 1 or x2==y2: continue # x2, y2가 무조건 더 커야하며, 차이는 최소 1 이어야함
                else: break
            num_4 = []
            num_4.append(x1)
            num_4.append(y1)
            num_4.append(x2)
            num_4.append(y2)
            res.append(num_4)
        return res