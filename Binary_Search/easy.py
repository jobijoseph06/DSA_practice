def Binary(arr, target):
    low = 0
    high = len(arr) -1
    while(low <= high):
        mid = (low + high) // 2
        if arr[mid] == target:
            return arr[mid]
        elif target > arr[mid]:
            low = mid +1
        else:
            high = mid - 1

print(Binary([3,4,6,7,9,12,16,17], 12))