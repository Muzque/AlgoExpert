def sortedSquaredArray(array):
    for idx, num in enumerate(array):
        array[idx] = num ** 2
    array.sort()
    return array
