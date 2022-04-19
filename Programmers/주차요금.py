import collections
import  math

fees = [120, 0, 60, 591]
records = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]

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
    totalMoney = fees[1]
    currentMin = i[1][1] - fees[0]
    if currentMin > 0:
        totalMoney += math.ceil(currentMin / fees[2]) * fees[3]

    answer.append(totalMoney)
print(answer)