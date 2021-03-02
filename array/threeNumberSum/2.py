def threeNumberSum(array, targetSum):
    array.sort()

    results = []
    for idx, num in enumerate(array):
        left, right = idx + 1, len(array) - 1
        while left < right:
            total = num + array[left] + array[right]
            if total == targetSum:
                results.append([num, array[left], array[right]])
                left += 1
                right -= 1
            elif total < targetSum:
                left += 1
            else:
                right -= 1
    return results
