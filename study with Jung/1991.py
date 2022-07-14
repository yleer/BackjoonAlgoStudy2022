import sys
import collections

tree = collections.defaultdict(list)

n = int(input())

for i in range(n):
    root, left, right = map(str, sys.stdin.readline().split())

    if left == "." and right == ".":
        tree[root] = [".","."]
    elif left == "." and right != ".":
        tree[root] = [".", right]
    elif left != "." and right == ".":
        tree[root] = [left, "."]
    else:
        tree[root] = [left, right]

# tree 완성.


def preorderSearch(node):
    print(node, end = "")

    nx = tree[node]

    if len(nx) == 0:
        return

    if nx[0] != ".":
        preorderSearch(nx[0])
    if nx[1] != ".":
        preorderSearch(nx[1])

preorderSearch("A")
print()


# print(tree)



def middleOrder(node):
    nx = tree[node]


    if nx[0] != ".":
        middleOrder(nx[0])



    print(node, end="")
    if nx[1] != ".":
        middleOrder(nx[1])


middleOrder("A")


print()

def postOrder(node):
    # print(node)
    nx = tree[node]


    if nx[0] != ".":
        postOrder(nx[0])
    if nx[1] != ".":
        postOrder(nx[1])


    print(node, end="")






postOrder("A")
