# 틀린 답
import random
num = int(input('number:'))

if num in range(1,101):
    a = random.randint(1,100)
    if num != a:
        if num > a:
            print('down')
        elif num < a:
            print('up')   
    else:
        print('bingo')
else:
    print('wrong number')
   
    
    
    
print('---------------------------------')

# 정답
import random
secret_num =random.randint(1,100)
print('answer:', secret_num)
i = 1
while i<=5:
    guess_num = int(input('number:'))
    if secret_num > guess_num:
        print('up')
    elif secret_num < guess_num:
        print('down')
    else:
        print('bingo')
        break
    i = i+1
print('the end')