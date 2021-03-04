def longestPeak(array):
    has_peak = False
    left = 0
    max_val = 0
    for right in range(1, len(array)):
        diff = array[right] - array[right - 1]
        if not has_peak and diff <= 0:
            if right - left > 1 and diff != 0:
                has_peak = True
            else:
                left = right
        elif has_peak and diff >= 0:
            has_peak = False
            max_val = max(max_val, right - left)
            left = right - 1 if diff > 0 else right
    if has_peak:
        return max(max_val, right - left + 1)
    return max_val
