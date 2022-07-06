atoms = [[80, 35], [70, 38], [100, 41], [75,30], [160,80], [77, 29], [181, 68], [151, 76]]
    #
maskCount = 0
maskUsedDate = 0

for i in range(len(atoms)):

    if maskUsedDate == 3:
        maskUsedDate = 0

    if atoms[i][0] >= 81 or  atoms[i][1] >= 36:
        if atoms[i][0] >= 151 and  atoms[i][1] >= 76:
            # print(i, maskCount, maskUsedDate)
            if maskUsedDate == 0:
                maskCount += 1
                maskUsedDate = 0
            elif maskUsedDate > 0:
                maskUsedDate = 0
            else:
                maskCount += 1
                maskUsedDate += 1
                # print(i)
        else:
            if maskUsedDate == 0:
                maskCount += 1
                maskUsedDate += 1
                # print(i)
            else:
                maskUsedDate+=1

    else:
        if 0 < maskUsedDate < 3:
            maskUsedDate += 1






print(maskCount)
