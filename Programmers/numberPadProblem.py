
distance = {
    "12":1,
    "15":2,
    "18":3,
    "10":4,
    "42":2,
    "45":1,
    "48":2,
    "40":3,
    "72":3,
    "75":2,
    "78":1,
    "70":2,
    "32":1,
    "35":2,
    "38":3,
    "30":4,
    "62":2,
    "65":1,
    "68":2,
    "60":3,
    "92":3,
    "95":2,
    "98":1,
    "90":2,
    "25":1,
    "28":2,
    "20":3,
    "52":1,
    "58":1,
    "50":2,
    "82":2,
    "85":1,
    "80":1,
    "02":3,
    "05":2,
    "08":1,

    "*1":0,
    "*2":4,
    "*4":0,
    "*5":3,
    "*7":0,
    "*8":2,
    "*0":1,


    "#3":0,
    "#2":4,
    "#6":0,
    "#5":3,
    "#9":0,
    "#8":2,
    "#0":1
}


# numbers, hand = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left"

numbers, hand = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"

answer = ""
leftHandStart = "*"
rightHandStart = "#"

leftNums = ["1","4","7"]
rifhtNums = ["3","6","9"]


for i in range(len(numbers)):
    # print(i,answer, leftHandStart, rightHandStart)
    leftHandStart = leftHandStart + str(numbers[i])
    rightHandStart = rightHandStart + str(numbers[i])

    targetNum = str(numbers[i])

    if targetNum in leftNums:
        answer.append("L")
        leftHandStart = targetNum
        rightHandStart = rightHandStart[0]
    elif targetNum in rifhtNums:
        answer.append("R")
        rightHandStart = targetNum
        leftHandStart = leftHandStart[0]
    else:
        if distance[leftHandStart] > distance[rightHandStart]:
            leftHandStart = leftHandStart[0]
            rightHandStart = rightHandStart[1]
            answer.append("R")
        elif distance[leftHandStart] < distance[rightHandStart]:
            leftHandStart = leftHandStart[1]
            rightHandStart = rightHandStart[0]
            answer.append("L")
        else:

            if hand == "right":
                leftHandStart = leftHandStart[0]
                rightHandStart = rightHandStart[1]
                answer.append("R")
            else:
                leftHandStart = leftHandStart[1]
                rightHandStart = rightHandStart[0]
                answer.append("L")
                answer = answer + "L"




a = "".join(answer)
print(a)
