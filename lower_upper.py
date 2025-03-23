s = "JoBi JOSepH"
s = s.strip()
og = ""
for char in s:
    number = ord(char)
    if 65<= number <= 90:
        number +=32
        og+=chr(number)
    else:
        number-=32
        og+=chr(number)
print(og)


