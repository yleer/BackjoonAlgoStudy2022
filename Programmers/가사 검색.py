import collections

words =["aa", "ac", "az"]
    #["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries =["a?"]
    # ["fro??", "????o", "fr???", "fro???", "pro?"]

dic = collections.defaultdict(int)

answer = [0 for _ in range(len(queries))]

for word in words:
    for i in range(len(word)):
        q = "?" * (len(word) - i)
        a = q + word[len(word) -i:]
        dic[a] += 1

        c = word[: i] + q
        if a == c:
            pass
        else:
            dic[c] += 1


print(dic)
for i in range(len(queries)):
    answer[i] = dic[queries[i]]

print(answer)