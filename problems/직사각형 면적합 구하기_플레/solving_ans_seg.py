import sys
input = sys.stdin.readline

MAXLEN = 100001
tree = [0]*(4*MAXLEN)
cnt = [0]*(4*MAXLEN)

def update(start, end, idx, l, r, val) :
  if r < start or end < l :
    return
  if l <= start <= end <= r :
    cnt[idx] += val
  else :
    mid = (start + end) // 2
    update(start, mid, idx<<1, l, r, val)
    update(mid+1, end, idx<<1|1, l, r, val)
  if cnt[idx] > 0 :
    tree[idx] = end - start + 1
  else :
    tree[idx] = tree[idx<<1] + tree[idx<<1|1]

N = int(input())
coord = []
for _ in range(N) :
    x1, y1, x2, y2 = map(int, input().split())
    coord.append((y1, x1, x2-1, 1))
    coord.append((y2, x1, x2-1, -1))

coord.sort()
prev = coord[0][0]
ret = 0
for y, l, r, val in coord :
    if prev != y :
        ret += tree[1] * (y - prev)
    prev = y
    update(0, MAXLEN-1, 1, l, r, val)
print(ret)