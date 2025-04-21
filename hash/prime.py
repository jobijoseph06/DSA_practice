def prime(n):
    count = 0
    for i in range(2, n):
        if n%i == 0:
            count +=1
    print("Count: ",count)
    if count == 0:
        return "Prime number"
    else:
        return "Not a prime number"

print(prime(2))