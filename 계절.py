# num = 10

# if num >= 1 and num < 4:
#     print('a')

# elif num >= 4 and num < 7:
#     print('b')

# else:
#     print('c')

# num = 4

# if 1 <= num < 4:
#     print('a')

# elif 4 <= num < 7:
#     print('b')

# else:
#     print('c')





# spring 3,4,5
# summer 6,7,8
# fall 9,10,11
# winter 12,1,2


# import datetime
# now = datetime.datetime.now()
# mon = now.month
# print(mon)



mon = int(input('current month:'))


if mon >= 3 and mon < 6:
    print('spring')
elif mon >= 6 and mon < 9:
    print('summer')
elif mon >= 9 and mon < 12:
    print('fall')
else:
    print('winter')