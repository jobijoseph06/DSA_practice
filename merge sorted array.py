def merge(arr1, arr2, m, n):
    total = m+n
    arr3 = [0] * total
    left = 0
    right = 0
    index = 0
    while left < m and right < n:
        if arr1[left] < arr2[right]:
            arr3[index] = arr1[left]
            index+=1
            left+=1
        else:
            arr3[index] = arr2[right]
            index += 1
            right+=1
    while left < m:
        arr3[index] = arr1[left]
        index+=1
    while right < n:
        arr3[index] = arr2[right]
        index+=1
        right+=1




    print(arr1)
    print(arr2)
    return arr3




print(merge([1,2,3,0,0,0], [2,5,6], 3, 3))
