arr = [0,3,7,2,5,8,4,6,0,1]
long = 1
arr1 = set(arr)
og_sub = []
for i,num in enumerate(arr):
    if num-1 not in arr1:
        length = 1
        temp = [num]
        while num+length in arr1:
            temp.append(num+length)
            length+=1
            if length > long:
                long = length
                og_sub = temp
print(long)
print(og_sub)
print(arr1)
