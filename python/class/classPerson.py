# 이름, 성별, 나이를 갖는 Person 클래스를 다음과 같이 정의하시오.
# 클래스 변수: 이름 네임, 성별 젠더, 나이 에이지
# 생성자: 멤버 변수(이름, 성별, 나이) 초기화
# 클래스 함수 디스플레이: 이름, 성별, 나이 출력 가능


class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
    def setName(self, name):
        self.name = name
    def setGender(self, gender):
        self.gender = gender
    def setAge(self, age):
        self.age = age

lilist = []

li = Person('amy', 'female', 14)
lilist.append(li)
li = Person('jun', 'male', 20)
lilist.append(li)
li = Person('rein', 'male', 18)
lilist.append(li)

for i in lilist:
    print(f'{i.name}\t{i.gender}\t{i.age}')
