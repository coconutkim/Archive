# 요구사항
# 1. 정수를 입력받으세요
# 2. 정수가 양의 정수, 0, 음의 정수
# 정수 = num

num = int(input('정수 입력>'))
# print(num)

if num > 0:
    print('양수입니다.')

if num == 0:
    print('0입니다.')

if num < 0:
    print('음수입니다.')

print('the end')