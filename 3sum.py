arr = [-1,0,1,2,-1,-4]
n = len(arr)
og = set()
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if arr[i]+arr[j]+arr[k] == 0:
               triplet = tuple(sorted([arr[i],arr[j],arr[k]]))
               og.add(triplet)
print(og)