def quickSort(sortList):
    if len(sortList) <= 1:
        return sortList
    else:
        pivot = sortList[0]
        less = [x for x in sortList[1:] if x < pivot]
        more = [x for x in sortList[1:] if x >= pivot]
        return quickSort(less) + [pivot] + quickSort(more)