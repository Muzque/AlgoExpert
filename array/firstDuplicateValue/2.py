def firstDuplicateValue(array):
    for num in array:
        positive = abs(num)
        if array[positive - 1] < 0:
            return positive
        array[positive - 1] *= -1
    return -1
