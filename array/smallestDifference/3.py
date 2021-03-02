def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()

    pt1, pt2 = 0, 0
    result = (float("inf"), [])
    while pt1 < len(arrayOne) and pt2 < len(arrayTwo):
        one = arrayOne[pt1]
        two = arrayTwo[pt2]
        if one > two:
            diff = one - two
            pt2 += 1
        elif two > one:
            diff = two - one
            pt1 += 1
        else:
            return [one, two]
        if diff <= result[0]:
            result = (diff, [one, two])
    return result[1]
