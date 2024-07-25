import random
a = input('number:')
a = int(a)

if a in range(1,101):
    a = random.randint(1,100)
    if a > 37:
        print('down')
    elif a < 37:
        print('up')
    else:
        print('bingo')
else:
    print('wrong number')