def xor(arr,b):
    n = len(arr)
    count = 0
    start = end = 0
    for i in range(n):
        xor = 0
        for j in range(i,n):
            xor ^= arr[j]
            if xor == b:
                count +=1
                start = i
                end = j
                print(arr[start:end+1])
    return count
print(xor([4, 2, 2, 6, 4], 6 ))