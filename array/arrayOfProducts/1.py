from functools import reduce


def arrayOfProducts(array):
    result = []
    for idx, num in enumerate(array):
        left = reduce(lambda x,y: x*y, array[:idx], 1)
        right = reduce(lambda x,y: x*y, array[idx+1:], 1)
        result.append(left*right)
    return result
