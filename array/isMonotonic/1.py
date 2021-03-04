def isMonotonic(array):
    if len(array) < 2:
        return True
    for idx in range(1, len(array)):
        if array[idx] != array[idx - 1]:
            start = idx
            is_ascend = array[idx] > array[idx - 1]
            break
    else:
        return True
    for idx in range(start, len(array)):
        if (is_ascend and array[idx] < array[idx - 1]) or (
            not is_ascend and array[idx] > array[idx - 1]
        ):
            return False
    return True
