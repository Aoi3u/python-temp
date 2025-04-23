def findSmallest(arr):
    smallest = arr[0]
    smallestIndex = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallestIndex = i
    return smallestIndex

def selectionSort(arr):
    sortedArr = []
    for i in range(len(arr)):
        smallestIndex = findSmallest(arr)
        sortedArr.append(arr.pop(smallestIndex))
    return sortedArr
