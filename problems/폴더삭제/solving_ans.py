def func(wallpaper):
    x,y = [], []
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == 'D':
                x.append(i)
                y.append(j)
    return [min(x), min(y), max(x)+1, max(y)+1]


n, m = map(int, input().split())
wallpaper = [input().rstrip() for _ in range (n)]

res = func(wallpaper)
# print(*res)
print(" ".join(map(str, res)))