n = str(input("Enter the number:"))
def find(n):
    count = 0
    for number in n:
        number = int(number)
        count+=number
    return str(count)
count = find(n)
# print(count)

if len(count) > 1:
    count = find(count)
if len(count) == 1:
    if count[-1] == str("1"):
        print("Magic number")
    else:
        print("Not a magic number")

