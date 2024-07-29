# def open_account():
#     print("새로운 계좌를 개설합니다.")

# open_account() # 앞에 정의한 open_account() 함수 호출
# open_account()

def deposit(balance, money):
    print('{0}원을 입금했습니다. 잔액은 {1}원입니다.'.format(money, balance+money))
    return balance + money

balance = deposit(10000, 1000)
# print(f'리턴된 값: {balance}')

def withdraw_night(balance, money): # 업무 시간 외 출금
    commission = 100 # 출금 수수료 100원
    print("업무 시간 외에 {}원을 출금했습니다." .format(money))
    return commission, balance - money - commission
    # 100, 11000-500-100

# 업무 시간 외 출금 시도
commission, balance = withdraw_night(balance, 500)
print("수수료 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))
