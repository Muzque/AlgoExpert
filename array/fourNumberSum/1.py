def fourNumberSum(array, targetSum):
    results = []
    init = array.pop(0)
    stacks = [(init, [init])]
    while array:
        num = array.pop(0)
        arr = [(stack[0]+num, stack[1] + [num])
               for stack in stacks] + [(num, [num])]
        for tup in arr:
            if len(tup[1]) < 4:
                stacks.append(tup)
            elif tup[0] == targetSum:
                results.append(tup[1])
    return results
