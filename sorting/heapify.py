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