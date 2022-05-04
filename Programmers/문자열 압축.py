# s = "xxxxxxxxxxyyy"
# # print(s[-2:])
# answers = [""] * (len(s) + 1)
# # print(answers)
# originS = s
# for i in range(len(s)):
#     i = i + 1
#     s = originS
#     while s:
#         if len(answers[i]) == 0:
#             if len(s) < i:
#                 answers[i] = answers[i] + s
#                 break
#             if s[:i] == s[i:i+i]:
#                 answers[i] = "2" + s[:i]
#                 s = s[i+i:]
#             else:
#                 answers[i] = s[:i]
#                 s = s[i:]
#
#         else:
#             if len(s) < i:
#                 answers[i] = answers[i] + s
#                 break
#
#             prevWord = answers[i][-i:]
#             if prevWord == s[:i]:
#                 if answers[i][-i-1] == "9":
#                     answers[i] = answers[i][:-i-1] + "1" + "0" + s[:i]
#                     s = s[i:]
#                 else:
#                     answers[i] = answers[i][:-i-1] + str(int(answers[i][-i - 1]) + 1) + answers[i][-i:]
#                     s = s[i:]
#             else:
#                 if s[:i] == s[i:i+i]:
#                     answers[i] = answers[i] + "2" + s[:i]
#                     s = s[i + i:]
#                 else:
#                     answers[i] = answers[i] + s[:i]
#                     s = s[i:]
#
#
# answers.pop(0)
# an = 1000
# for it in answers:
#     print(it, len(it))
#
#     an = min(len(it), an)
#
# print(an)







s = "aabbaccc"

answer = [0 for _ in range(len(s))]

# print(answer)


for i in range(len(s)):
    tmp = ""
    tmpS = s


    i = i + 1

    while tmpS:
        if len(tmp) == 0:
            curr = tmpS[:i]
            nex = tmpS[i: i+i]
            if curr != nex:
                tmp += curr
                tmpS = tmpS[i:]
            else:
                tmp = "2" + curr
                tmpS = tmpS[i+i:]
        else:
            prev = tmp[-i:]
            curr = tmpS[:i]

            if prev == curr:
                nums = ""
                for char in tmp[-i-i:-i]:
                    if char.isalpha():
                        pass
                    else:
                        nums += char

                str(int(nums) + 1)
                tmp = [:-i]
                tmpS = tmpS[i:]
            else:
                tmp += curr
                tmpS = tmpS[i:]

    # answer[i-1] = tmp
    answer[i-1] = len(tmp)














