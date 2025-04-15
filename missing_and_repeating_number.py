def repeating(arr):
    freq = [0] * len(arr)
    print(freq)
    for num in arr:
        freq[num-1] +=1
    repeat = 0
    missing = 0
    for i in range(len(freq)):
        if freq[i] == 0:
            missing = i+1
        if freq[i] == 2:
            repeat = i+1
    return [repeat, missing]
print(repeating([1,2,3,6,7,5,7]))




























