import datetime

now = datetime.datetime.now()
print('{}년 {}월 {}일'.format(now.year, now.month, now.day))
print('{}시 {}분 {}초'.format(now.hour, now.minute, now.second))


# if now.hour < 12:
#     print('오전')

# if now.hour >= 12:
#     print('오후')

if now.hour < 12:
    print('오전')

else:
    print('오후')