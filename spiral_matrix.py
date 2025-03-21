mat = [[1,2,3],[4,5,6],[7,8,9]]
left= 0
top= 0
right = len(mat[0]) - 1
bottom = len(mat) -1
# print(right,bottom)
og = []
while left <= right and top <= bottom:
    for i in range(left,right+1):
        og.append(mat[top][i])
    top+=1
    for i in range(top,bottom+1):
        og.append(mat[i][right])
    right-=1
    if top <= bottom:
        for i in range(right,left-1,-1):
            og.append(mat[bottom][i])
        bottom-=1
    if left <= right:
        for i in range(bottom,top-1,-1):
            og.append(mat[i][left])
        left+=1
print(og)
