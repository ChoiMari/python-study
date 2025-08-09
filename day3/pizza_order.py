# 피자 주문 실습
s_pizza_size: int = 15
m_pizza_size: int = 20
l_pizza_size: int = 25
s_pepperoni: int = 2
ml_pepperoni: int = 3
cheese: int = 1
bill:int = 0

print("Python Pizza 배달에 오신 것을 환영합니다!")
select_pizza_size: str = input("어떤 크기의 피자를 원하시나요? S, M, L \n")
select_add_peppperoni: str = input("피자에 페퍼로니를 추가하시겠습니까? Y 또는 N \n")
select_extra_cheese: str = input("추가 치즈를 원하시나요? Y 또는 N \n")

if select_pizza_size == "S":
    bill += s_pizza_size
    if select_add_peppperoni == "Y":
        bill += s_pepperoni
    if select_extra_cheese == "Y":
        bill += cheese
elif select_pizza_size == "M":
    bill += m_pizza_size
    if select_add_peppperoni == "Y":
        bill += ml_pepperoni
    if select_extra_cheese == "Y":
        bill += cheese
elif select_pizza_size == "L":
    bill += l_pizza_size
    if select_add_peppperoni == "Y":
        bill += ml_pepperoni
    if select_extra_cheese == "Y":
        bill += cheese
else:
    print("잘못된 입력입니다.")
print(f"최종 결제 금액은 ${bill}입니다.")






