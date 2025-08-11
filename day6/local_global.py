# 지역변수 & 전역변수
gun = 10

def check_point(soldiers:int) -> None :
    global gun # 전역변수 gun을 함수 내에서 사용하겠다고 명시
    gun -= soldiers #global gun 안쓰면 에러발생 : UnboundLocalError
    print(f"[함수 내] 남은 총 : {gun}")

print(f"전체 총 : {gun}")
check_point(2)
print(f"남은 총 : {gun}")