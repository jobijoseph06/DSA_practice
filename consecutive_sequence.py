nums = [100,5, 4, 200, 1, 3, 2]
long = 0
for num in nums:
    if num-1 not in nums:
        length = 1
        while num + length in nums:
            length+=1
            if length > long:
                long = length
print(long)

