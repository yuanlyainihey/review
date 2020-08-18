def bubbleSort(sortList):
    for i in range(len(sortList)-1):
        for j in range(i+1, len(sortList)):
            if sortList[i] > sortList[j]:
                sortList[i], sortList[j] = sortList[j], sortList[i]
    return sortList