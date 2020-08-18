def shellSort(sortList):
    length = len(sortList)
    gap = length // 2
    print(sortList)
    while gap > 0:
        print(gap)
        for i in range(gap, length):
            tmp = sortList[i]
            j = i - gap
            while j >= 0 and sortList[j] > tmp:
                sortList[j + gap] = sortList[j]
                j -= gap
            sortList[j + gap] = tmp
            print(sortList)
        gap //= 2
    return sortList