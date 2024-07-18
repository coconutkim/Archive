ttime = input("주어진 시간:")
study = input("하루 공부 시간:")
ttime = int(ttime)
study = int(study)

a = ttime//study//365
b = ttime//study%365
c = ttime%study

print("{0}년 {1}일 {2}시간동안 화이팅하세요.".format(a, b, c))
