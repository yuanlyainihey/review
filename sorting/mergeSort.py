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