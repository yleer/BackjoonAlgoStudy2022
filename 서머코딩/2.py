import collections
import heapq

rooms = ["[403]James", "[404]Azad,Louis,Andy", "[101]Azad,Guard"]
target = 403
def calucateMinLength(arr, target):
    minLen = 100000
    for a in arr:
        minLen = min(abs(target-a), minLen)
        if minLen == 1:
            return 1
    return minLen

bannedPerson = []

dic = collections.defaultdict(list)

for room in rooms:
    closeIn = room.index("]")
    roomNum = int(room[1:closeIn])

    people = room[closeIn + 1:].split(",")
    for person in people:
        if target != roomNum:
            dic[person].append(roomNum)
        else:
            bannedPerson.append(person)


lenths = [[] for _ in range(1000)]

maxLen = 0

for key, value in dic.items():
    if key not in bannedPerson:
        maxLen = max(len(value), maxLen)
        lenths[len(value)].append(key)

lenths = lenths[1: maxLen+1]
answer = []

for sameLen in lenths:
    t = []
    for p in sameLen:
        # heapq.heappush(t, [calucateMinLength(dic[p],target), p])
        t.append([calucateMinLength(dic[p],target), p])

    t = heapq.heapify(t)
    for i in range(len(t)):
        a = heapq.heappop(t)
        answer.append(a[1])

print(answer)

