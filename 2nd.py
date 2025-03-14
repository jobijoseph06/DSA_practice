arr =[12,456,6,7,89,23,5,456]
n = len(arr)
for i in range(n-1):
    for j in range(n-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)

for num in range(n-2,-1,-1):
    if arr[num] < arr[-1]:
        print(arr[num])
        break