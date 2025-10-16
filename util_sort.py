def sort_list(array, swap_predicate):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if swap_predicate(array[j], array[j+1]):
                array[j], array[j+1] = array[j+1], array[j]
    return array