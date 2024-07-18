# 클래스 기초문제 2
# 은행계좌 클래스를 작성하세요./
# 1. 클래스명을 Account 라고 합니다./
# 2. 내용에는 은행명, 예금주, 계좌번호,
# 잔고 가 있습니다./
# 3. bank, name, accountNumber, balance/
# 4. 저금하는 멤버함수를 만들어주세요.deposit금액/
# 5. 인출하는 멤버함수를 작성해주세요.withdraw금액/
# 6. 계좌정보를 출력하는 멤버함수를 작성하세요. display_info

# 우리은행 박위비 74857-993-0029 200000 wori(인스턴스 이름)
# 신한은행 김영호 94833-003399   170000 shin

class Account:
    def __init__(self, bank, name, accountNumber, balance):
        self.bank = bank
        self.name = name
        self.accountNumber = accountNumber
        self.balance = balance
    def deposit(self, pay):
        self.balance+=pay
    def withdraw(self, pay):
        if self.balance >= pay:
            self.balance-=pay
        else:
            print('잔고가 부족합니다.')
    def display_info(self):
        print(f'현재 {self.name}님의 잔고는 {self.balance}원입니다.' )

wori = Account('우리은행', '박위비', '74857-993-0029', 200000)
shin = Account('신한은행', '김영호', '94833-003399', 170000)

wori.deposit(500)
wori.withdraw(200500)
shin.withdraw(8000)
wori.display_info()
shin.display_info()