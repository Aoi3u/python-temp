def quicksort(array):
    if len(array) < 2:
        return array
    pivot = array[0]
    # arrayの要素1以降で、pivotより小さいグループと、pivotより大きいグループの2つに振り分け
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)

