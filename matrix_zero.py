mat = [[1,1,1],[1,0,1],[1,1,1]]
row  = len(mat) * [0]
col  = len(mat[0]) * [0]
for i in range(len(row)):
    for j in range(len(col)):
        if mat[i][j] == 0:
            row[i] = 1
            col[j] = 1
print(row)
print(col)
for i in range(len(row)):
    for j in range(len(col)):
        if row[i] == 1 or col[j]:
            mat[i][j] = 0
print(mat)