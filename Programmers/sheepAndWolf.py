import collections


edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
info = [0,0,1,1,1,0,1,0,1,0,1,1]

print("SDf")


tree = collections.defaultdict(list)
for edge in edges:
    tree[edge[0]].append(edge[1])

sheeps = 1
wolf = 0
visited = [0]

able = []
def bfs(location):
    global sheeps, wolf, visited, able


    if info[location] == 0:
       visited.append(location)
       sheeps += 1
       nextLoc = tree[location]
       for ne in nextLoc:
           bfs(ne)
    else:
        if sheeps <= wolf + 1:
            able = able + tree[location]
        else:
            nextLoc = tree[location]
            for ne in nextLoc:
                bfs(ne)




bfs(0)
print(able, visited)
print(sheeps,wolf)



