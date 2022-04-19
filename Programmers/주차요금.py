import collections
fees = [180, 5000, 10, 600]
records = [
    "05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT",
    "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
    "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"
]

def timeSubtraction(bigger,smaller):
    bigH = bigger[:2]
    bigM = bigger[3:]

    smallH = smaller[:2]
    smallM = smaller[3:]

    if bigH == smallH:
        return int(bigM) - int(smallM)
    else:
        if bigM >= smallM:
            return int(bigM) - int(smallM) + (int(bigH) - int(smallH)) * 60
        else:
            int(bigH) - 1
            return 60 - int(smallM) + int(bigM) + (int(bigH) - 1 - int(smallH)) * 60



usedTime = collections.defaultdict(list)


inList = []

for record in records:
    a = record.split(" ")
    # print(a)
    if a[2][0] == "I":
        inList.append(a[1])
        prev = usedTime[a[1]]
        if len(prev) == 0:
            usedTime[a[1]] = [a[0], 0]
        else:
            usedTime[a[1]] = [a[0], prev[1]]
    else:
        # out
        inList.remove(a[1])
        curr = usedTime[a[1]]
        # need to take care of time sub
        inTime = timeSubtraction(a[0], curr[0])
        usedTime[a[1]] = [0, curr[1] + inTime]


print(inList)

print(usedTime)



for key,value in usedTime.items():
    if value[0] != 0:
        dif = timeSubtraction("23:59", value[0])
        value[1] = value[1] + dif
        value[0] = 0
        value = value[1]


sorted_dict = sorted(usedTime.items())
print(sorted_dict)

answer = []
for i in sorted_dict:
    print(i[1][1])