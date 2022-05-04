import  collections
import copy
# fares = 	[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
fares = [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]
dic = collections.defaultdict(list)
for far in fares:
    dic[far[0]].append([far[1],far[2]])
    dic[far[1]].append([far[0], far[2]])



def bfs(curr, visted, cost, dst,result):
    if curr in visted:
        return result

    if curr == dst:
        result.append(cost)
        return result


    origin = cost
    for nextLoc in dic[curr]:
        cost = origin
        cost = cost + nextLoc[1]

        if len(result) > 0:
            if min(result) < cost:
                return result
        new = copy.deepcopy(visted)
        new.append(curr)

        bfs(nextLoc[0], new, cost,dst,result)

    return result

n = 6
s = 4
a = 5
b = 6


totalANs = []
def allBfs(curr, visited, cost,a,b):
    # print(visited, curr,"11")
    if curr in visited:
        return
    # print(visited, curr, "22")
    if curr == b:

        an1 =[]
        ttt = copy.deepcopy([])
        bfs(curr, ttt, 0 , a,an1)
        totalANs.append(min(an1) + cost)
        return
    elif curr == a:
        ttt = copy.deepcopy([])
        an2 = []
        bfs(curr, ttt, 0 , b,an2)
        totalANs.append(min(an2) + cost)
        return
    # bfs(curr, visted, cost, dst, result)

    aAns = []
    bAns = []

    t = copy.deepcopy([])
    t2 = copy.deepcopy([])
    cc = 0
    bfs(curr, t, 0, b, bAns)
    bfs(curr, t2, 0, a, aAns)

    if len(aAns) > 0 and len(bAns) > 0:
        # print(cost,min(aAns) ,min(bAns))
        cc = cost + min(aAns) + min(bAns)
    else:
        if len(aAns) == 0 and len(bAns) > 0:
            cc = cost + min(bAns)
        elif len(aAns) > 0 and len(bAns) == 0:
            cc = cost + min(aAns)
        elif len(aAns) == 0 and len(bAns) == 0:
            cc = cost

    # if len(totalANs) > 0:
    #     if cc > min(totalANs):
    #         return

    if cc != 0:

        totalANs.append(cc)


    oriCo = cost
    for rout in dic[curr]:
        c = copy.deepcopy(visited)
        c.append(curr)
        cost = oriCo
        cost += rout[1]
        print(curr, visited,rout, "whjjag;")

        allBfs(rout[0],c,cost,a,b)



allBfs(4,copy.deepcopy([]),0,a,b)
print(totalANs)
print(min(totalANs))











