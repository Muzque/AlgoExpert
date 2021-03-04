def twoNumberSum(array, targetSum):
    cache = {}
    for n in array:
        cache[n] = cache.get(n, 0) + 1
    for a, count in cache.items():
        b = targetSum - a
        if cache.get(b) is not None and (a != b or count > 1):
            return [a, b]
    return []
