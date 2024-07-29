scr = int(input('Your score:'))

if scr >= 90 and scr <= 100:
    print('A')
elif scr >= 80 and scr < 90:
    print('B')
elif scr >= 70 and scr < 80:
    print('C')
elif scr >= 0 and scr < 70:
    print('F')
else:
    print('점수는 0점에서 100점 사이로 입력하세요')