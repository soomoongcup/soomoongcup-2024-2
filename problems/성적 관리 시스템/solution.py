from __future__ import annotations

import sys


SCORE_2_GRADE = "FDCBA"
DEFAULT_SCORE = 3


def score_clamp(score: int) -> int:
    return max(0, min(4, score))


def make_node(name: str) -> int:
    global node_prev, node_next, node_name
    node_prev.append(None)
    node_next.append(None)
    node_name.append(name)
    return len(node_prev)-1


def list_name_of(node_id: int) -> str:
    # O(N)
    global node_prev
    while node_prev[node_id] is not None:
        node_id = node_prev[node_id]
    return node_name[node_id]


def list_is_empty(list_id: int) -> bool:
    # O(1)
    return list_head[list_id] == node_prev[list_tail[list_id]]


def list_count(list_id: int) -> int:
    # O(N)
    global node_next, list_head, list_tail
    node_id = list_head[list_id]
    count = 0
    while (node_id := node_next[node_id]) != list_tail[list_id]:
        count += 1
    return count


def list_insert_list(src_list_id: int, dst_list_id: int) -> None:
    # O(1)
    global node_prev, node_next, list_head, list_tail
    if (src_list_id == dst_list_id) or list_is_empty(src_list_id):
        return
    src_lnode_id = node_next[list_head[src_list_id]]
    src_rnode_id = node_prev[list_tail[src_list_id]]
    dst_lnode_id = list_head[dst_list_id]
    dst_rnode_id = node_next[list_head[dst_list_id]]
    # 네 개의 노드 연결
    node_prev[dst_rnode_id] = src_rnode_id
    node_next[dst_lnode_id] = src_lnode_id
    node_prev[src_lnode_id] = dst_lnode_id
    node_next[src_rnode_id] = dst_rnode_id
    # src list 는 비우기
    node_next[list_head[src_list_id]] = list_tail[src_list_id]
    node_prev[list_tail[src_list_id]] = list_head[src_list_id]


def list_insert_node(list_id: int, node_id: int) -> None:
    # O(1)
    global node_prev, node_next, list_head, list_tail
    # 기존의 리스트에서 노드 제거
    lnode_id = node_prev[node_id]
    rnode_id = node_next[node_id]
    node_prev[rnode_id] = lnode_id
    node_next[lnode_id] = rnode_id
    # 새로운 리스트로 노드 삽입
    lnode_id = list_head[list_id]
    rnode_id = node_next[lnode_id]
    node_prev[rnode_id] = node_id
    node_next[lnode_id] = node_id
    node_prev[node_id] = lnode_id
    node_next[node_id] = rnode_id


N, M = map(int, sys.stdin.readline().split())

node_prev = [None] * (N+1)
node_next = [None] * (N+1)
node_name = [None] * (N+1)

list_head = [make_node(SCORE_2_GRADE[score]) for score in range(5)]
list_tail = [make_node(SCORE_2_GRADE[score]) for score in range(5)]

for score in range(5):
    head = list_head[score]
    tail = list_tail[score]
    node_next[head] = tail
    node_prev[tail] = head

for x in range(1, N+1):
    node_prev[x] = x-1
    node_next[x] = x+1

node_prev[1] = list_head[DEFAULT_SCORE]
node_next[N] = list_tail[DEFAULT_SCORE]
node_prev[list_tail[DEFAULT_SCORE]] = N
node_next[list_head[DEFAULT_SCORE]] = 1

for i in range(M):
    cmd, *args = sys.stdin.readline().split()
    if cmd == 'SET':
        x, y = map(int, args)
        list_insert_node(list_id=y, node_id=x)
    elif cmd == 'ADD':
        y, z = map(int, args)
        list_insert_list(src_list_id=y, dst_list_id=score_clamp(y+z))
    elif cmd == 'PRN':
        x = int(args[0])
        name = list_name_of(x)
        sys.stdout.write(name+'\n')
    elif cmd == 'CNT':
        y = int(args[0])
        count = list_count(y)
        sys.stdout.write(str(count)+'\n')
