def reverse(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > 2 * arr[j]:
                print(i,j)
                print(arr[i],arr[j])
                count+=1
    return count
print(reverse( [6, 4, 1, 2, 7]))