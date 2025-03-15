def solve(num):
    result = [[1]]
    for i in range(num-1):
        summa = []
        temp = [0] + result[-1] + [0]
        for i in range(len(temp)-1):
            summa.append(temp[i] + temp[i+1])
        result.append(summa)

    return result
print(solve(5))
