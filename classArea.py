# 요구조건
# - 인스턴스를 선언할 때 가로, 세로 길이를 받을 수 있는 클래스를 선언해 주세요
# - 인스턴스에서 사각형, 삼각형, 원의 넓이를 구하는 메소드를 생성해주세요
# - 원의 넓이를 계산할 때는 세로 길이는 무시하고, 가로 길이를 원의 지름이라 가정하고 계산해 주세요
# 출처: https://woong-garden.tistory.com/entry/18-파이썬-class-문제-풀이 [새싹:티스토리]

class Area:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def square(self):
        return self.a * self.b
    def triangle(self):
        return self.a * self.b / 2
    def circle(self):
        return (self.a / 2)**2 * 3.14
    
a, b = map(float, input("가로와 세로 길이를 입력하세요:").split())
area = Area(a, b)
print(area.square())
print(area.triangle())
print(area.circle())
