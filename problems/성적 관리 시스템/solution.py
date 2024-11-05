from __future__ import annotations

import dataclasses
import sys
import typing


@dataclasses.dataclass
class Node:
    prev: typing.Optional[Node] = None
    next: typing.Optional[Node] = None

    @property
    def is_head(self) -> bool:
        return False

    def head(self) -> Head:
        node = self
        while not node.is_head:
            node = node.prev
        return node


@dataclasses.dataclass
class Head(Node):
    lst: LinkedList = None
    prev = None

    @property
    def is_head(self) -> bool:
        return True


@dataclasses.dataclass
class Tail(Node):
    lst: LinkedList = None
    next = None


def node_link(left: Node, right: Node) -> None:
    left.next, right.prev = right, left


class LinkedList:
    def __init__(self, grade: str) -> None:
        self.grade = grade
        self.head = Head(lst=self)
        self.tail = Tail(lst=self)
        node_link(self.head, self.tail)

    def __len__(self) -> int:
        count = 0
        node = self.head.next
        while node is not self.tail:
            count += 1
            node = node.next
        return count

    def is_empty(self) -> bool:
        return self.head.next is self.tail

    def add_node(self, node: Node) -> None:
        if node.prev is not None and node.next is not None:
            node_link(node.prev, node.next)
        node_link(self.tail.prev, node)
        node_link(node, self.tail)

    def add_list(self, other: LinkedList) -> None:
        if other.is_empty():
            return
        node_link(self.tail.prev, other.head.next)
        node_link(other.tail.prev, self.tail)
        node_link(other.head, self.tail)


def solve(N: int, M: int, instructions: typing.List[str]) -> typing.List[str]:
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
        grades[-1].add_node(students[i])
    answers = []
    for line in instructions:
        cmd, *args = line.split()
        if cmd == 'SET':
            x, y = map(int, args)
            node = students[x-1]
            grades[y].add_node(node)
        elif cmd == 'ADD':
            y, z = map(int, args)
            grades[y].add_list(grades[max(min(4, y+z), 0)])
        elif cmd == 'PRN':
            x = int(args[0])
            node = students[x-1]
            answers.append(node.head().lst.grade)
        elif cmd == 'CNT':
            y = int(args[0])
            answers.append(str(len(grades[y])))
    return answers


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    instructions = sys.stdin.readlines()
    ans = solve(N, M, instructions)
    sys.stdout.write('\n'.join(ans))
