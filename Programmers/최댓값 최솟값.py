s ="-1 -1"

a = s.split()

tmp = []
for num in a:
    tmp.append(int(num))

tmp.sort()


print(str(tmp[0]) + " " + str(tmp[-1]))

