import collections

gems =["XYZ", "XYZ", "XYZ"]

min_nums = 10000
number_gems = len(set(gems))
end = 0

jewerys = collections.defaultdict(int)

for start, gem in enumerate(gems):

    while len(jewerys) < number_gems and end < len(gems):
        jewerys[gems[end]] += 1
        end += 1


    if len(jewerys) == number_gems:
        if min_nums > end - start:
            min_nums = end - start
            result = [start + 1, end]

    jewerys[gem] -= 1
    if jewerys[gem] == 0:
        del(jewerys[gem])

print(result)




