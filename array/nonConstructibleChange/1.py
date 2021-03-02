def nonConstructibleChange(coins):
    if not coins:
        return 1
    queue = [coins.pop(0)]
    while coins:
        coin = coins.pop(0)
        queue += [num + coin for num in queue] + [coin]
    queue = set(queue)
    a = dict.fromkeys(queue)
    b = dict.fromkeys(range(1, len(a) + 1))
    c = dict.fromkeys(x for x in b if x not in a)
    if not c:
        return len(b) + 1
    return list(c.keys())[0]
