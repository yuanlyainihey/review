def countSort(sortList):
    minVal = maxVal = sortList[0]
    for x in sortList:
        if x < minVal:
            minVal = x
        if x > maxVal:
            maxVal = x
    countList = [0] * (maxVal - minVal + 1)
    print(countList)
    for item in sortList:
        countList[item - minVal] += 1
    idx = 0
    print(countList)
    for count in range(maxVal-minVal+1):
        for num in range(countList[count]):
            sortList[idx] = count + minVal
            idx += 1
    return sortList