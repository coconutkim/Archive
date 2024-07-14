# 요구조건
# - 설정한 숫자를 계산해줄 클래스를 선언해주세요
# - 메소드를 호출해서 num1, num2를 설정할 수 있도록 해주세요
# - 입력된 숫자의 더하기, 빼기, 곱하기, 나누기 연산 결과를 구하는 메소드를 생성해주세요
# 출처: https://woong-garden.tistory.com/entry/18-파이썬-class-문제-풀이 [새싹:티스토리]

class Calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def plus(self):
        return self.a + self.b
    def minus(self):
        return self.a - self.b
    def multiple(self):
        return self.a * self.b
    def divide(self):
        return self.a / self.b
    
a, b = map(float, input('두 개의 숫자를 입력해주세요:').split())
calc = Calc(a, b)
print(calc.plus())
print(calc.minus())
print(calc.multiple())
print(calc.divide())