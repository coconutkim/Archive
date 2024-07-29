numbers = [1,2,3,4,5,6,7,8,9]
output = [[], [], []]

# print('성공' if True else '실패')


for number in numbers:
    output[(number-1)%3].append(number)



for number in numbers:
    output[(number+2)%3].append(number)

print(output)

