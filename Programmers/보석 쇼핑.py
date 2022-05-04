# # import collections
# #
# # gems =["XYZ", "XYZ", "XYZ"]
# #
# # min_nums = 10000
# # number_gems = len(set(gems))
# # end = 0
# #
# # jewerys = collections.defaultdict(int)
# #
# # for start, gem in enumerate(gems):
# #
# #     while len(jewerys) < number_gems and end < len(gems):
# #         jewerys[gems[end]] += 1
# #         end += 1
# #
# #
# #     if len(jewerys) == number_gems:
# #         if min_nums > end - start:
# #             min_nums = end - start
# #             result = [start + 1, end]
# #
# #     jewerys[gem] -= 1
# #     if jewerys[gem] == 0:
# #         del(jewerys[gem])
# #
# # print(result)
# #
# #
# #
# #
#
#
#
#
#
#
#
#
# import collections
#
# gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
# num = len(set(gems))
#
# print(num)
#
# stored = []
#
# start = 0
# end = 0
#
# dup = []
#
# for i in range(len(gems)):
#     if i == 0:
#         stored.append(gems[i])
#     else:
#         if gems[i] not in stored:
#             stored.append(gems[i])
#             end += 1
#         else:
#             dup.append()
#
#
#
#
#
#
#
#
#
#


class Counter:
    _ncreated = 0
    def __init__(self, color = "black", initValue = 0):
        self.__count = initValue
        self.__color = color

        Counter._ncreated += 1
    def reset(self):
        self.__count = 0

    def increment(self):
        self.__count += 1

    def get(self):
        return  self.__count
    def __eq__(self, other):
        return self.__count == other.__counter

    def __str__(self):
        return "dasf"

a = Counter(100)
b = Counter()

print(a)


