def insertion(arr,target):
    low =0
    high = len(arr) - 1
    while(low<=high):
        mid = (low+high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid +1


    return  low



print(insertion([1,3,5,6], 5.5))