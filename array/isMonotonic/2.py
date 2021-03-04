def isMonotonic(array):
    if len(array) < 3:
        return True
    direction = None
    for idx in range(1, len(array)):
        diff = array[idx] - array[idx - 1]
        if diff == 0:
            continue
        if direction is None:
            direction = diff > 0
        if direction != (diff > 0):
            return False
    return True
