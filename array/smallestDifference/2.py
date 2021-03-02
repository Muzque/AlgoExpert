def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()

    left, right = 0, 0
    result = (float("inf"), [])
    while left < len(arrayOne) and right < len(arrayTwo):
        diff = abs(arrayOne[left] - arrayTwo[right])
        if diff < result[0]:
            result = (diff, [arrayOne[left], arrayTwo[right]])
        if right < len(arrayTwo) - 1:
            right += 1
        else:
            left += 1
            right = 0
    return result[1]
