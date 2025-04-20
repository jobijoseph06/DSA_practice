def Floor_and_ceil(arr, target):
    first = -1
    last = -1
    low, high = 0, len(arr)-1
    while low<=high:
        mid = (low+high) // 2
        if arr[mid] <= target:
            first = arr[mid]
            low = mid+1
        else:
            high = mid-1
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= target:
            last = arr[mid]
            high = mid - 1

        else:
            low = mid + 1

    return first, last
print(Floor_and_ceil([3, 4, 4, 7, 8, 10], 2))