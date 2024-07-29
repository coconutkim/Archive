numbers = [273,103,5,32,65,9,72,800,99]

# for number in numbers:
#     if number >= 100:
#         print('- 100 이상의 수:',number)





# for number in numbers:
#     if number % 2 ==0:
#         print(f'{number} 는 짝수입니다.')
#     else:
#         print(f'{number} 는 홀수입니다')





for number in numbers:
    # if 0 < number <10:
    #     print(f'{number} 는 1 자릿수입니다.')
    # elif 10 <= number <100:
    #     print(f'{number} 는 2 자릿수입니다.')
    # else:
    #     print(f'{number} 는 3 자릿수입니다.')


    print(f'{number} 는 {len(str(number))} 자릿수입니다.')