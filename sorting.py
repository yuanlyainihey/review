testList = [7, 8, 9, 4, 5, 6, 1, 2, 3]
testListDupNum = [7, 7, 2, 3, 7, 4, 5, 8, 2]


def bubbleSort(sortList):
    for i in range(len(sortList)-1):
        for j in range(i+1, len(sortList)):
            if sortList[i] > sortList[j]:
                sortList[i], sortList[j] = sortList[j], sortList[i]
    return sortList


def selectionSort(sortList):
    for i in range(len(sortList)-1):
        minIdx = i
        for j in range(i+1, len(sortList)):
            if sortList[j] < sortList[minIdx]:
                minIdx = j
        sortList[i], sortList[minIdx] = sortList[minIdx], sortList[i]
    return sortList


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


def mergeSort(sortList):
    if len(sortList) <= 1:
        return sortList
    mid = len(sortList) // 2
    left = mergeSort(sortList[:mid])
    right = mergeSort(sortList[mid:])
    return merge(left, right)


def merge(left, right):
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result


def quickSort(sortList):
    if len(sortList) <= 1:
        return sortList
    else:
        pivot = sortList[0]
        less = [x for x in sortList[1:] if x < pivot]
        more = [x for x in sortList[1:] if x >= pivot]
        return quickSort(less) + [pivot] + quickSort(more)


def heapify(arr):
    n = len(arr)
    for i in reversed(range(n // 2)):
        # shiftDown(arr, n, i)        # 从大到小
        shiftUp(arr, n, i)          # 从小到大


def shiftDown(arr, n, k):       # 大堆顶
    while 2 * k + 1 < n:
        j = 2 * k + 1
        if j + 1 < n and arr[j + 1] < arr[j]:
            j += 1      # 选取两个叶节点中比较小的那个的下标
        if arr[k] <= arr[j]:
            break
        arr[k], arr[j] = arr[j], arr[k]
        k = j


def shiftUp(arr, n, k):         # 小堆顶
    while 2 * k + 1 < n:
        j = 2 * k + 1
        if j + 1 < n and arr[j + 1] > arr[j]:
            j += 1      # 选取两个叶节点中比较大的那个的下标
        if arr[k] >= arr[j]:
            break
        arr[k], arr[j] = arr[j], arr[k]
        k = j


def heapSort(sortList):
    n = len(sortList)
    heapify(sortList)
    for i in range(n):
        sortList[n-i-1],sortList[0] = sortList[0],sortList[n-i-1]
        # shiftDown(sortList, n-i-1, 0)   # 从大到小排列
        shiftUp(sortList, n-i-1, 0)     # 从小到大排列
    return sortList


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


def sysSort(sortList):
    sortList.sort()
    # sortList.sort(reverse=True)       // 降序
    return sortList


if __name__ == '__main__':
    # print(bubbleSort(testList))
    # print(selectionSort(testList))
    # print(insertionSort(testList))
    # print(shellSort(testList))
    # print(mergeSort(testList))
    # print(quickSort(testList))
    print(heapSort(testList))
    # print(countSort(testListDupNum))
    # print(sysSort(testList))