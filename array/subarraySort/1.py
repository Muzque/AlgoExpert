def subarraySort(array):
    bot, top = float('inf'), -float('inf')
    for i in range(1, len(array)):
        j = len(array) - i - 1
        if array[i] < array[i - 1] and array[i] < bot:
            bot = array[i]
        if array[j] > array[j + 1] and array[j] > top:
            top = array[j]
    left, right = -1, -1
    for i in range(len(array)):
        j = len(array) - i - 1
        if array[i] > bot and left == -1:
            left = i
        if array[j] < top and right == -1:
            right = j
    return [left, right]
