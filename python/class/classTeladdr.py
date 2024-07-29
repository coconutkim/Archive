# 클래스 기초문제 1

# 전화번호 클래스를 작성하세요./
# 1. 이름, 나이, 전화번호를 기본적으로 작성합니다./
# 2. 클래스명을 telAddr 라고 합니다./
# 3. telBook 라는 리스트를 생성해서 클래스를 저장하세요.
# 4. telBook 을 저장하세요.
# 5. 클래스 telAddr 에는 이름, 나이, 전화번호를 지정하는
# 멤버함수를 작성해주세요.  setName(), setAge(), setTel()

# 순희 24 010-625-9928
# 철수 36 010-536-9019
# 말희 40 010-893-0092
# 순신 26 010-772-9920

# 6. telBook = []    telBook.append(인스턴스)
# 추가 테스트 사항
# 추가1. 순희의 이름을 영희로 바꿔주세요.

class telAddr:
    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
    def setName(self, name):
        self.name = name
    def setAge(self, age):
        self.age = age
    def setTel(self, tel):
        self.tel = tel

telBook = []

te = telAddr("순희", 24, "010-625-9928")
telBook.append(te)
te = telAddr("철수", 36, "010-536-9019")
telBook.append(te)
te = telAddr("말희", 40, "010-893-0092")
telBook.append(te)
te = telAddr("순신", 26, "010-772-9920")
telBook.append(te)

telBook[0].setName("영희")
telBook[2].setAge(41)

for i in telBook:
    print(f'{i.name} {i.age} {i.tel}')
# print(telBook[0].name)
