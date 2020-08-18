def selectionSort(sortList):
    for i in range(len(sortList)-1):
        minIdx = i
        for j in range(i+1, len(sortList)):
            if sortList[j] < sortList[minIdx]:
                minIdx = j
        sortList[i], sortList[minIdx] = sortList[minIdx], sortList[i]
    return sortList