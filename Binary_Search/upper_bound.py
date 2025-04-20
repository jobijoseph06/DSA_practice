def upper(arr, target):
    n = len(arr)
    low,high,result = 0,n-1,0
    while(low<=high):
        mid = (low+high) //2
        if arr[mid] > target:
            high = mid-1
        else:
            low = mid+1
    arr.insert(low, target)
    return arr,low
print(upper( [45, 60, 60, 60, 70, 85, 90], 46))

