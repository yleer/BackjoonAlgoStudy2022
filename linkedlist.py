class Node:
    def __init__(self):
        self.removed = False
        self.prev = None
        self.next = None


def solution(n, k, cmd):
    nodeArray = [Node() for _ in range(n)]

    for i in range(1, n):
        nodeArray[i-1].next = nodeArray[i]
        nodeArray[i].prev = nodeArray[i-1]

    curr = nodeArray[k] # 현재 노드

    # 이전 노드로 돌아가기
    for _ in range(3):
        curr = curr.prev

    # 앞 노드로 가기
    for _ in range(3):
        curr = curr.next


    # 삭제
    front = curr.next
    prev = curr.prev

    if front:
        front.prev = prev
    if prev:
        prev.next = front


    