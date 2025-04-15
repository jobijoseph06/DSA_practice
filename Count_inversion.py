def count_inversion(arr):
    count = 0
    for left in range(len(arr)):
        for right in range(left+1, len(arr)):
            if arr[left] > arr[right]:
                count+=1
    return count
print(count_inversion( [-10, -5, 6, 11, 15, 17]))