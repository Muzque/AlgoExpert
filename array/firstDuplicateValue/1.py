def firstDuplicateValue(array):
    cached = set()
    for num in array:
        if num in cached:
            return num
        cached.add(num)
    return -1
