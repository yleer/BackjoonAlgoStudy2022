
st = input()


nums = []
indexOfOPluse = []
indexOfMinus = []

tmp = ""
for i in range(len(st)):

    if st[i] == '+':
        if len(tmp) > 0:
            nums.append(int(tmp))
            tmp = ""
        indexOfOPluse.append(len(nums))
    elif st[i] == '-':
        if len(tmp) > 0:
            nums.append(int(tmp))
            tmp = ""
        indexOfMinus.append(len(nums))
    else:
        tmp = tmp + st[i]


if len(tmp) > 0:
    nums.append(int(tmp))
    tmp = ""



sum = 0

sub = 0
subs = []
for i in range(0, len(indexOfMinus)):
    if i + 1 < len(indexOfMinus):
        a = list(range(indexOfMinus[i], indexOfMinus[i+1]))
        for ch in a:
            subs.append(ch)


if len(indexOfMinus) > 0:
    tt = list(range(indexOfMinus[-1], len(nums)))
    for z in tt:
        subs.append(z)

sum = 0
for i in range(len(nums)):
    if i in subs:
        sum = sum - nums[i]
    else:
        sum = sum + nums[i]


print(sum)