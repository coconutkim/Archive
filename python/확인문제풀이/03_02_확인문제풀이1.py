# x = 10
# y = 2

# if x > 4:
#     if y > 2:
#         print(x*y)

# else:
#     print(x+y)


# # if 2개를 and로 이어줄 수 있다
# if x>10:
#     if x<20:
#         print('조건에 맞습니다')


# -------------------------------------------------------


import datetime

now = datetime.datetime.now()

input = input('입력:')
# 공백을 넣어도 작동할 수 있도록
input = input.strip()
hello = '안녕'
time = '몇 시'

# if문에 바로 '안녕', '몇 시' 넣어도 작동함
if hello in input:
    print('> 안녕하세요.')

# 띄어쓰기 신경쓸 것 (예. 몇 시 != 몇시)
elif time in input:
    print(f'> 지금은 {now.hour}시입니다.')



