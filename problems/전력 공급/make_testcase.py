from random import randint

class Calculate:
    def __init__(self, n):
        self.n = n
    
    def values(self):
        row_values = []

        N = randint(1, 300)
        row_values.append(N)

        for _ in range(N):
            M = randint(1, 100000)
            row_values.append(M)
        
        matrix = [[0] * N for _ in range(N)] # 2차원 배열 형태로 만들고

        for i in range(N):
            for j in range(i + 1, N): # 대각선의 오른쪽 상단만 처리
                value = randint(1, 100000)
                matrix[i][j] = value
                matrix[j][i] = value

        return row_values, matrix

