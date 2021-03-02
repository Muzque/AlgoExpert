def smallestDifference(arrayOne, arrayTwo):
    result = ()
    while arrayTwo:
        new = arrayTwo.pop()
        for num in arrayOne:
            current = abs(num - new)
            if not result or current < result[0]:
                result = (current, [num, new])
    return result[1]
