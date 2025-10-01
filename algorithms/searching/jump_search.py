from math import sqrt

def jump_search(arr, target):
    jump = int(sqrt(len(arr)))
    min_index = 0
    max_index = 0
    for i in range(0, len(arr), jump):
        if arr[i] == target:
            return i
        elif arr[i] < target:
            min_index = i
        else:
            max_index = i
            break
    if max_index == 0:
        max_index = len(arr)

    result_arr = arr[min_index:max_index]

    for el in range (len(result_arr)):
        if result_arr[el] == target:
            return el + min_index
    return -1
