def isValidSubsequence(array, sequence):
    pt = sequence.pop(0)
    for n in array:
        if n == pt:
            try:
                pt = sequence.pop(0)
            except:
                return True
    return False
