import collections
alp = 10
cop = 10
problems = [[10,15,2,1,2],[20,20,3,3,4]]


solvingSequences = []
for i in range(len(problems)):
    solvingSequences.append([problems[i][0] + problems[i][1], i])
solvingSequences.sort()




def minminStudy(study, curAlp, curCop, targetAlp, targetCop):


    needAlp = targetAlp - curAlp
    needCop = targetCop - curCop

    if needAlp <= 0 and needCop <= 0:
        return  [0,0,0]

    maxNeedTime = targetAlp + targetCop

    for i in range(1,maxNeedTime+1):

        for a in study[i]:
            if a[0] >= needAlp and a[1] >= needCop:
                return [a[0], a[1], i]


        for j in range(1,i+1):
            k = i - j

            study[j]
            study[k]

            for it in study[j]:

                if it[0] >= needAlp and it[1] >= needCop:
                    return [it[0], it[1],j]

                for first in study[k]:
                    if [it[0] + first[0], it[1] + first[1]] not in study[i]:
                        study[i].append([it[0] + first[0], it[1] + first[1]])
                        if it[0] + first[0] >= needAlp and it[1] + first[1] >= needCop:
                            return [it[0] + first[0], it[1] + first[1], i]

                    if it[0] + first[0] >= needAlp and it[1] + first[1] >= needCop:
                        # needCop== [needAlp, needCop]:

                        # print(study)
                        # print("zzzzzzzzz", [it[0] + first[0], it[1] + first[1], i], "adsf", needAlp, needCop)

                        return [it[0] + first[0], it[1] + first[1], i]




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










