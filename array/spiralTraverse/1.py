def spiralTraverse(array):
    result = array.pop(0)
    idx_col = -1
    idx_row = None
    while array:
        try:
            if idx_col is None:
                arr = array.pop(idx_row)
                if idx_row == -1:
                    arr.reverse()
                result.extend(arr)
                idx_row = 0 if idx_row == -1 else -1
            else:
                direction = 1 if idx_col == -1 else -1
                for arr in array[::direction]:
                    result.append(arr.pop(idx_col))
            idx_row, idx_col = idx_col, idx_row
        except:
            break
    return result
