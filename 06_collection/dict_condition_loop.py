# 딕셔너리와 조건문, 반복문
# 조건문
# - 딕셔너리가 비어있는지 확인하기
# - 특정 키가 존재하는지 확인하기
my_dict = {}
# None, 0, 0.0, "", [], (), {}, set() 모두 Flase 취급
if my_dict:
    print("비어있지 않음")  # 실행안함

my_dict2 = {"name": "철수"}
if my_dict2:
    print("비어있지 않음")
else:
    print("비어있음")

# 딕셔너리에 in을 사용하면 기본적으로 key를 검사한다
print("name" in my_dict2)
# name이라는 키가 my_dict2에 존재하는지 확인

if "name" in my_dict2:
    print("name 키가 존재합니다.")
else:
    print("name 키가 존재하지 않음")

# 반복문
# - 딕셔너리의 자체를 순회하기

# 키 존재 여부 확인 목적이라면
# 굳이 keys()쓰지 않는 것이 일반적
# 그냥 in 연산자 쓰면 됨
user = {"name": "홍길동", "age": 14, "gender": "m"}
for key in user:
    print(key, end=" ")  # name age gender

print()
# 딕셔너리.keys() 키 목록 반환
# -> 순회는 그냥 in 연산자 쓰는게 권장

# 딕셔너리.values() 값 순회
for value in user.values():
    print(value, end=" ")  # 홍길동 14 m

print()

# 딕셔너리.items() 키와 값을 동시에 순회
for key, value in user.items():
    print(f"{key}: {value}", end=", ")
    # name: 홍길동, age: 14, gender: m,

print()

# 반복문 + 조건문
# 딕셔너리의 키와 값이 특정
for key, value in user.items():
    if key == "name":
        print(f"{key}는 {value}입니다.")
    else:
        print(f"{key}:{value}")


# 딕셔너리 컴프리헨션
# 딕셔너리를 간결하게 생성하는 문법
# 조건문과 반복문을 활용하여 딕셔너리를 생성
# 1~5까지의 숫자를 키로 하고, 그 숫자의 제곱을
# 값으로 하는 딕셔너리 생성
# 기본
# {key: value for 변수 in 반복객체}
# 조건 포함
# {key: value for 변수 in 반복객체 if 조건}
squared_dict = {n: n**2 for n in range(1, 6)}
print(squared_dict)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
