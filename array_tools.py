def find_max(arr):
    biggest = arr[0]
    for x in arr:
        if x > biggest:
            biggest = x
    return biggest


def find_min(arr):
    smallest = arr[0]
    for x in arr:
        if x < smallest:
            smallest = x
    return smallest


def count_item(arr, item):
    count = 0
    for x in arr:
        if x == item:
            count += 1
    return count


def reverse_list(arr):
    i = 0
    j = len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr


def remove_duplicates(arr):
    unique = []
    for x in arr:
        if x not in unique:
            unique.append(x)
    return unique


def partition(arr, pivot):
    smaller = []
    equal = []
    bigger = []
    for x in arr:
        if x < pivot:
            smaller.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            bigger.append(x)
    return (smaller, equal, bigger)


def sort_list(arr):
    data = arr[:]
    for i in range(len(data)):
        min_index = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_index]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
    return data


def kth_smallest(arr, k):
    # k starts from 1
    data = arr[:]
    value = None
    for i in range(k):
        value = find_min(data)
        data.remove(value)
    return value
