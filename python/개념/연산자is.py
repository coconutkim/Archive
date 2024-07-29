a = 1
b = 1
while a<500:
    print(a is b,a,b)
    a = a+1
    b = b+1
    if not (a is b):
        break