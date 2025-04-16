def max_product(arr):
    max = arr[0]
    for i in range(len(arr)):
        current = 1
        for j in range(i,len(arr)):
            current*=arr[j]
            if current > max:
                max = current
                
    return max


print(max_product([2,3,-2,4]))
print(max_product([-2,0,-1]))