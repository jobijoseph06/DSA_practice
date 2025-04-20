def find(arr, element):
    result = []
    for i,number in enumerate(arr):
        if number == element:
            result.append(i)
    if len(result) == 1:
        return [result[0], result[0]]
    if len(result) == 0:
        return [-1,-1]

    return [result[0], result[-1]]
print(find([2,4,6,8,8,11,13], 8))
