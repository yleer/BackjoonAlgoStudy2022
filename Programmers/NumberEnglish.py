

dic = {
    "zero" : 0,
    "one" : 1,
    "two": 2,
    "three" : 3,
    "four" :4,
    "five" :5,
    "six" : 6,
    "seven" : 7,
    "eight" :8,
    "nine" : 9
}


s = "2three45sixseven"

answer = []
temp = ""
for char in s:
    if char.isalpha():
        temp += char
        if temp in dic.keys():
            answer.append(str(dic[temp]))
            temp = ""
    else:

        if temp in dic.keys():
            answer.append(str(dic[temp]))
            temp = ""
        answer.append(str(char))
        temp = ""
print(answer)

a = int("".join(answer))
print(a)