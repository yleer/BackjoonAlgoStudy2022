import collections
alp = 10
cop = 10
problems = [[10,15,2,1,2],[20,20,3,3,4]]


solvingSequences = []
for i in range(len(problems)):
    solvingSequences.append([problems[i][0] + problems[i][1], i])
solvingSequences.sort()




def minminStudy(study, curAlp, curCop, targetAlp, targetCop):
    # print(study,"z")
    needAlp = targetAlp - curAlp
    needCop = targetCop - curCop

    if needAlp <= 0 and needCop <= 0:
        return  [0,0,0]

    maxNeedTime = targetAlp + targetCop




    for i in range(2,maxNeedTime+1):
        print(i,targetAlp,targetCop, needAlp, needCop, curAlp, curCop)
        print(study)
        prev = study[i-1]

        for it in prev:

            if it[0] >= needAlp and it[1] >= needCop:
                return [it[0], it[1], i-1]
            for first in study[1]:

                if [it[0] + first[0], it[1] + first[1]] not in study[i]:
                    study[i].append([it[0] + first[0], it[1] + first[1]])

                if it[0]+first[0] >= needAlp and  it[1]+first[1] >= needCop:
                # needCop== [needAlp, needCop]:

                    print("zzzzzzzzz",[it[0]+first[0], it[1]+first[1], i])

                    return [it[0]+first[0], it[1]+first[1], i]


        if i % 2 == 0:
            tmp = study[int(i / 2)]
            for t in range(len(tmp)):
                for k in range(t,len(tmp)):

                    if [tmp[t][0] + tmp[k][0], tmp[t][1] + tmp[k][1]] not in study[i]:
                        study[i].append([tmp[t][0] + tmp[k][0], tmp[t][1] + tmp[k][1]])

                    if tmp[t][0] + tmp[k][0] >= needAlp and tmp[t][1] + tmp[k][1] >= needCop:
                        print("asdfasdfadsf", [tmp[t][0] + tmp[k][0], tmp[t][1] + tmp[k][1], i])
                        return [tmp[t][0] + tmp[k][0], tmp[t][1] + tmp[k][1], i]




time = 0

studyable = collections.defaultdict(list)
studyable[1] = [[1,0],[0,1]]

for i in range(len(solvingSequences)):

    currentProblem = problems[solvingSequences[i][1]]

    if alp >= currentProblem[0] and cop >= currentProblem[1]:
        time += currentProblem[4]
        alp += currentProblem[2]
        cop +=  currentProblem[3]
        studyable[currentProblem[4]].append([currentProblem[2],currentProblem[3]])


    else:
        result = minminStudy(studyable, alp, cop, currentProblem[0],currentProblem[1])

        time += result[2]
        alp += result[0]
        cop += result[1]
        studyable[currentProblem[4]].append([currentProblem[2],currentProblem[3]])

        print(alp, cop, time)
    print(alp, cop, time)

print(time)











{
    1: [[1, 0], [0, 1]], 2: [[2, 0], [1, 1], [0, 2], [2, 1]],
    3: [[3, 0], [2, 1], [1, 2], [0, 3], [3, 1], [2, 2]],
    4: [[4, 0], [3, 1], [2, 2], [1, 3], [0, 4], [4, 1], [3, 2], [2, 3], [4, 2]],
    5: [[5, 0], [4, 1], [3, 2], [2, 3], [1, 4], [0, 5], [5, 1], [4, 2], [3, 3], [2, 4], [5, 2], [4, 3]],
    6: [[6, 0], [5, 1], [4, 2], [3, 3], [2, 4], [1, 5], [0, 6], [6, 1], [5, 2], [4, 3], [3, 4], [2, 5], [6, 2], [5, 3], [4, 4]],
    7: [[7, 0], [6, 1], [5, 2], [4, 3], [3, 4], [2, 5], [1, 6], [0, 7], [7, 1], [6, 2], [5, 3], [4, 4], [3, 5], [2, 6], [7, 2], [6, 3], [5, 4], [4, 5]],
    8: [[8, 0], [7, 1], [6, 2], [5, 3], [4, 4], [3, 5], [2, 6], [1, 7], [0, 8], [8, 1], [7, 2], [6, 3], [5, 4], [4, 5], [3, 6], [2, 7], [8, 2], [7, 3], [6, 4], [5, 5], [4, 6], [8, 3], [7, 4], [6, 5], [8, 4]],
    9: [[9, 0], [8, 1], [7, 2], [6, 3], [5, 4], [4, 5], [3, 6], [2, 7], [1, 8], [0, 9], [9, 1], [8, 2], [7, 3], [6, 4], [5, 5], [4, 6], [3, 7], [2, 8], [9, 2], [8, 3], [7, 4], [6, 5], [5, 6], [4, 7], [9, 3], [8, 4], [7, 5], [6, 6], [9, 4], [8, 5]],
    10: [[10, 0], [9, 1], [8, 2], [7, 3], [6, 4], [5, 5], [4, 6], [3, 7], [2, 8], [1, 9], [0, 10], [10, 1], [9, 2], [8, 3], [7, 4], [6, 5], [5, 6], [4, 7], [3, 8], [2, 9], [10, 2], [9, 3], [8, 4], [7, 5], [6, 6], [5, 7], [4, 8], [10, 3], [9, 4], [8, 5], [7, 6], [6, 7], [10, 4], [9, 5], [8, 6]]}
)