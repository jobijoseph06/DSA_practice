arr = [3,2,3]
n = len(arr)
result = {}
for num in arr:
    if num not in result:
        result[num] = 1
    else:
        result[num]+=1
for key,value in result.items():
    if value > n // 3:
        print(key)

