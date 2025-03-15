def find(arr,k):
    count = 0
    for i in range(len(arr)):
        sum = 0
        for j in range(i,len(arr)):
            sum+=arr[j]
            if sum == k:
                count+=1
    return count
print(find([1,2,3],3))
print(find([1,-1,0],0))