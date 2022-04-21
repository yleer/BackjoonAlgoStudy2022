new_id = "123_.def"

print(new_id.lower())
new_id = new_id.lower()
tmp = ""
for char in new_id:
    if char == "-" or char =="." or char == "_" or char.isalnum():
        tmp += char
# print(tmp)
tmp2 = ""
for char in tmp:
    if len(tmp2) == 0:
        tmp2 += char
    else:

        if char == "." and tmp2[-1] == "." :
            pass
        else:
            tmp2 += char
# print(tmp2)

if tmp2[0] == ".":
    tmp2 = tmp2[1:]

# print(tmp2,"Sadf")
if len(tmp2) == 0:
    tmp2 += "a"
if tmp2[-1] == ".":
    tmp2 = tmp2[:-1]
# print(tmp2)

if len(tmp2) == 0:
    tmp2 += "a"

if len(tmp2) >= 16:
    tmp2 = tmp2[:15]

if tmp2[-1] == ".":
    tmp2 = tmp2[:-1]

if len(tmp2) <= 2:
    while len(tmp2) < 3:
        tmp2 = tmp2 + tmp2[-1]


