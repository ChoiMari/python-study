# 지역변수 & 전역변수
gun = 10 # 전역변수

def check_point(soldiers:int) -> None :
    global gun # 전역변수 gun을 함수 내에서 사용하겠다고 명시
    gun -= soldiers #global gun 안쓰면 에러발생 : UnboundLocalError
    print(f"[함수 내] 남은 총 : {gun}")

print(f"전체 총 : {gun}")
check_point(2)
print(f"남은 총 : {gun}")

#전역변수 사용은 코드관리가 어렵기 때문에 권장하는 방법은 아니다!

# 가급적 함수의 전달 값으로 파라미터로 던져서 연산을 하고 반환 값을 받아서 사용하는 방법을 사용한다고..
# 다음과 같은 방식이 권장됨
def check_point_ret(gun:int, soldiers:int) -> None :
    gun -= soldiers #파라미터로 선언된 gun 지역변수
    print(f"[함수 내] 남은 총 : {gun}")
    return gun

gun = check_point_ret(gun, 2) # 전역변수 값을 아규먼트로 넣어서 호출함
# 반드시 리턴값을 받아서 저장을 시켜야 전역변수 값이 바뀐다.
print(f"남은 총 : {gun}") #전역변수 값 출력