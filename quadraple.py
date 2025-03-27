arr =  [1,0,-1,0,-2,2]
og = set()
n = len(arr)
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1, n):
            for l in range(k+1, n):
                if arr[i]+arr[j]+arr[k]+arr[l] == 0:
                    og.add((arr[i], arr[j],arr[k],arr[l]))
print(og)
