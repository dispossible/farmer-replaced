def sort_list(array, swap_predicate):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if swap_predicate(array[j], array[j+1]):
                array[j], array[j+1] = array[j+1], array[j]
    return array


def array_2d(x_size, y_size, value = None):
    arr = []
    for x in range(x_size):
        arr.append([])
        for y in range(y_size):
            arr[x].append(value)
    return arr