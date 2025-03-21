string = "Hello@world!#$%^&*"
# print(ord('a'))
for char in string:
    if ('A' <= char <= 'Z') or ('a' <= char <='z') or ('0' <= char <='9'):
        continue
    else:
        print(char,end="")
        # print(char,end="")
