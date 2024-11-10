def ans(n, list_board):
    board = [[0 for _ in range(103)] for _ in range(103)]

    cnt = 0

    for k in range(n):
        x1, y1, x2, y2 = list_board[k]
        for i in range(x1, x2):
            for j in range(y1, y2):
                if board[i][j] == 1: continue
                board[i][j] = 1
                cnt += 1
    # print(cnt)
    return cnt

# n = int(input())
# list_board = [list(map(int, input().split())) for _ in range(n)]
# print(ans(n, list_board))