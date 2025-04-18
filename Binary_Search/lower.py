def lower(arr, target):
    n = len(arr)
    low, high = 0, n-1
    result = 0
    while(low<=high):
        mid = (low+high) // 2
        if arr[mid] >= target:
            result = mid
            high = mid-1
        else:
            low = mid+1
    arr.insert(result, target)

    return arr,result
print(lower([45, 60, 60, 60, 70, 85, 90],65))

