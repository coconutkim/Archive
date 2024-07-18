def toDay(tim):
    return tim/24

def toYear(dy):
    return dy // 365, dy % 365

ti = input("시간을 입력해 주세요:")

day = toDay(int(ti))
year, rem = toYear(day)

print(f"{int(year)}년", end="")
print(f"{int(rem)}일")