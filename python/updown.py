# 틀린 답
# import random
# num = int(input('number:'))

# if num in range(1,101):
#     a = random.randint(1,100)
#     if num != a:
#         if num > a:
#             print('down')
#         elif num < a:
#             print('up')   
#     else:
#         print('bingo')
# else:
#     print('wrong number')
   
    
    
    
print('---------------------------------')

# 정답
import random

secret_num =random.randint(1,100)
guess_num = random.randint(1,100)
print(secret_num,guess_num)

# i = 1
# i = i+1
def f1():
    while True:
        if secret_num > guess_num:
            return 'up'
        elif secret_num < guess_num:
            return 'down'
        if secret_num == guess_num:
            return 'bingo'
            break
print(f'answer:{secret_num}/number:{guess_num}/{f1()}\n')
        
        
# import statistics
# a = [i for i in range(1,101)]
# a = statistics.median(a)
# print(a)
    