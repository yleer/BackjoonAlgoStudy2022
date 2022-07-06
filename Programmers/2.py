import collections

queue1 = [1, 2, 1, 2]
queue2 =  [1, 10, 1, 2]

queue1 = collections.deque(queue1)
queue2 = collections.deque(queue2)

total = sum(queue1) + sum(queue2)
targetNum = int(total / 2)

if targetNum != total / 2:
    print("-1")



count = 0

q1Sum = sum(queue1)
q2Sum = sum(queue2)

for i in range(len((queue1))*3):
    if q1Sum > q2Sum:
        tmp = queue1.popleft()
        q1Sum = q1Sum - tmp
        q2Sum = q2Sum + tmp
        queue2.append(tmp)
        count += 1
    elif q1Sum < q2Sum:
        tmp = queue2.popleft()
        q2Sum = q2Sum - tmp
        q1Sum = q1Sum + tmp
        queue1.append(tmp)
        count += 1


    if q1Sum == q2Sum:
        print("asn")
        break


print(count)