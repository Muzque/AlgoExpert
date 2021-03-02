def threeNumberSum(array, targetSum):
    array.sort()

    results = []
    init = array.pop(0)
    queue = [([init], init)]
    while array:
        new = array.pop(0)
        arr = [(q[0] + [new], q[1] + new) for q in queue]
        queue.append(([new], new))
        for tp in arr:
            if len(tp[0]) < 3:
                queue.append(tp)
            elif tp[1] == targetSum:
                results.append(tp[0])
    results.sort()
    return results
