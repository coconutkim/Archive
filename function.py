#두 개의 인수를 입력받아 더하는 함수를 작성하세요.

# 1. 함수명은 sum으로 한다.
# 2. 매개변수는 2개의 int 값으로 한다.
# 3. 함수는 2개의 매개변수를 더해서 반환한다.
# 4. 반환된 값을 인쇄하세요.

# valSum = sum(2, 3)
# print(f'더한 값은 {sum()}입니다.')

def sum(a, b):
    sum = a+ b
    return sum

valSum = sum(2, 3)
print(f'더한 값은 {valSum}입니다.')





# 사이트 url을 출력하는 함수를 만드세요
# (닷컴사이트)

# 1. 함수명은 make_url입니다.
# 2. url을 출력하세요.
# 3. 사용은 다음과 같이 할 예정입니다.

# url = make_url('naver')
# print(f'url은 {url} 입니다.')

def make_url(ut):
    url = "www" + ut + ".com"
    return url

url = make_url('naver')
print(f'URL은 {url} 입니다.')