def moveElementToEnd(array, toMove):
    left, right = 0, len(array) - 1
    while right > left:
        if array[left] == toMove:
            if array[right] != toMove:
                array[left], array[right] = array[right], array[left]
                right -= 1
                left += 1
            else:
                right -= 1
        else:
            left += 1
    return array
