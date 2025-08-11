#함수 정의
def open_account():
    print("새로운 계좌가 생성되었습니다.")

#함수 호출
open_account()

# 반환값이 있는 함수
def deposit(balance:int, money:int) -> int :
    print(f"입금이 완료되었습니다.\n잔액은 {balance + money}원 입니다.")
    return balance + money
def with_draw(balance:int, money:int) -> int :
    if balance < money :
        print("잔액이 부족하여 출금이 불가합니다.\n확인 후 다시 이용해주시길 바랍니다.")
        return 
    print(f"출금이 완료되었습니다.\n남은 잔액은 {balance - money}원 입니다.")
    return balance - money

balance = 0
balance = deposit(balance, 100)
print("잔액: {}".format(balance))
with_draw(balance, 110)