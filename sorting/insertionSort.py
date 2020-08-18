def insertionSort(sortList):
    for i in range(1, len(sortList)):
        if sortList[i] < sortList[i-1]:
            tmp = sortList[i]
            idx = i
            for j in range(i-1, -1, -1):
                if sortList[j] > tmp:
                    sortList[j+1] = sortList[j]
                    idx = j
            sortList[idx] = tmp
    return sortList