def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1
    pos = 0
    while low <= high:
        if arr[high] == arr[low]:
           if arr[low] == target:
               return low +1
           else:
               return -1
           
        pos = int(low + ((target - arr[low]) * (high - low) ) / (arr[high] - arr[low]))

        if pos < low or pos > high:
            return -1

        if arr[pos] == target:
            return pos + 1
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1


        

