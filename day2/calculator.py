# 팁 계산기
print("안녕하세요, 팁을 계산해 드리겠습니다.")
total = int(input("계산서의 총 금액이 얼마입니까? ")) 
tip = int(input("팁을 몇 %로 주고 싶으십니까? 10 12 15 \n")) 
people =int(input("몇 사람이 나눠서 계산 하십니까? ")) 

result = (total + (total * (tip / 100))) / people
print(f"각 사람이 내야할 금액은? {result}입니다")

# 주의) input함수는 문자열을 반환한다
# 연산할 때 변환 필요함

# 파이썬은 변수에 데이터 타입을 명시하지 않아서 헷갈리는데..??
# 변수 타입 힌트 문법이 있다!!
# 변수명: 타입 = 값

total2 : int = int(input("팁을 몇 %로 주고 싶으십니까? 10 12 15 \n"))
age: int = 25
price: float = 19.99
name: str = "홍길동"