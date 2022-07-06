
dic = {
    "R":0,
    "T":0,
    "C":0,
    "F":0,
    "J":0,
    "M":0,
    "A":0,
    "N":0
}

survey = ["TR", "RT", "TR"]
choices = [7,1,3]





for i in range(len(choices)):
    cur = survey[i]
    if choices[i] > 4:
        dic[cur[1]] = dic[cur[1]] + choices[i] - 4
    elif choices[i] < 4:
        dic[cur[0]] = dic[cur[0]] + 4 - choices[i]


answer = ""

if dic["R"] >= dic["T"]:
    answer = answer + "R"
else:
    answer = answer + "T"

if dic["C"] >= dic["F"]:
    answer = answer + "C"
else:
    answer = answer + "F"

if dic["J"] >= dic["M"]:
    answer = answer + "J"
else:
    answer = answer + "M"

if dic["A"] >= dic["N"]:
    answer = answer + "A"
else:
    answer = answer + "N"

print(answer)


