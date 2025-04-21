def first_and_last(arr, target):
    low, high = 0, len(arr)-1
    first = -1
    last = -1
    while low<=high:
        mid = (low+high) //2
        if arr[mid] <= target:
            first = mid
            low = mid+1

