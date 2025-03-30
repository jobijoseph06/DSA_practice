arr =[15, -2, 2, -8, 1, 7, 10, 23]
n = len(arr)
maxi = 0
s=e=0
for i in range(n):
    sum = 0
    for j in range(i, n):
        sum += arr[j]
        if sum == 0:
            if maxi < j-i+1:
                maxi = j-i+1
                s = i
                e = j
print(maxi)
print(arr[s:e+1])
print(chr(65))
print(chr(97))
print(chr(48))

