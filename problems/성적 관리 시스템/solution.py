from __future__ import annotations

import dataclasses
import sys
import typing


@dataclasses.dataclass
class Node:
    prev: typing.Optional[Node] = None
    next: typing.Optional[Node] = None
    is_head: bool = False
    is_tail: bool = False

    def get_head(self) -> Head:
        node = self
        while not node.is_head:
            node = node.prev
        return node


@dataclasses.dataclass
class Head(Node):
    list: LinkedList = None
    prev = None
    is_head: bool = True
    is_tail: bool = False


@dataclasses.dataclass
class Tail(Node):
    list: LinkedList = None
    next = None
    is_head: bool = False
    is_tail: bool = True


class LinkedList:
    def __init__(self, grade: str) -> None:
        self.grade = grade
        self.head = Head(list=self)
        self.tail = Tail(list=self)
        node_link(self.head, self.tail)

    def __len__(self) -> int:
        count = 0
        node = self.head.next
        while not node.is_tail:
            count += 1
            node = node.next
        return count

    def __repr__(self) -> str:
        return f'<LinkedList grade={self.grade!r}, count={len(self)}>'

    def is_empty(self) -> bool:
        return self.head.next is self.tail


def move_all_nodes(src: LinkedList, dst: LinkedList) -> None:
    if src == dst:
        return
    node_link(src.tail.prev, dst.head.next)
    node_link(dst.head, src.head.next)
    node_link(src.head, src.tail)


def move_node(node: Node, dst: LinkedList) -> None:
    node_link(node.prev, node.next)
    node_link(dst.tail.prev, node)
    node_link(node, dst.tail)


def node_link(left: Node, right: Node) -> None:
    if left is not None and right is not None:
        left.next, right.prev = right, left


def clamp(x: int, lo: int, hi: int) -> int:
    return max(lo, min(hi, x))


N, M = map(int, sys.stdin.readline().split())

students = [Node() for _ in range(N)]
grades = {
    4: LinkedList('A'),
    3: LinkedList('B'),
    2: LinkedList('C'),
    1: LinkedList('D'),
    0: LinkedList('F'),
    -1: LinkedList('-'),
}

for i in range(N):
    move_node(students[i], grades[-1])

for i in range(M):
    cmd, *args = sys.stdin.readline().split()
    if cmd == 'SET':
        x, y = map(int, args)
        node = students[x-1]
        move_node(node, grades[y])
    elif cmd == 'ADD':
        y, z = map(int, args)
        move_all_nodes(grades[y], grades[clamp(y+z, lo=0, hi=4)])
    elif cmd == 'PRN':
        x = int(args[0])
        node = students[x-1]
        sys.stdout.write(node.get_head().list.grade+'\n')
    elif cmd == 'CNT':
        y = int(args[0])
        sys.stdout.write(str(len(grades[y]))+'\n')
