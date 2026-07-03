# 리스트와 조건문 반복문
# 조건문
# - 리스트가 비어있는지 확인하기
# 0, 0.0, '', [], {}, set() 등은 모드 False로 간주된다.
my_list = [1, 2, 3]
if my_list:
    print("리스트가 비어있지 않습니다")
else:
    print("리스트가 비어있습니다.")  # 실행됨

my_list2 = []  # False로 간주
if my_list2:
    print("리스트가 비어있지 않습니다")
else:
    print("리스트가 비어있습니다.")  # 실행

# 리스트에 특정 값이 있는지 확인
# in 키워드 사용하여 특정 값이 포함되는지 확인할 수 있음
print("가" in ["가", "나", "다"])  # True
print(77 in [1, 2, 3, 4])  # False

if 2 in my_list:
    print("2가 있습니다")  # 실행됨

# 반복문
# while 루프를 사용할 수도 있지만, 리스트 순회할 때는
# for 루프가 일반적
# 리스트와 조건문, 반복문을 함께 사용하기
for fruit in ["사과", "포도", "바나나"]:
    if fruit == "포도":
        print("포도는 보라색")

# 리스트 컴프리헨션
# 리스트 컴프리헨션은 기존 반복 가능한 데이터를 기반으로
# 새로운 리스트를 생성하는 방법
# 문법: [표현식 for 항목 in 반복가능한데이터 if 조건]

# 예시1: 1부터 10까지의 숫자를 포함하는 리스트 생성
num_list = [x for x in range(1, 11)]
print(num_list)
# 예시2: 1부터 10까지의 숫자 중에서 짝수만 포함하는 리스트 생성
even_list = [x for x in range(1, 11) if x % 2 == 0]
print(even_list)
# 예시3: 리스트에서 특정 값이 있는지 확인하고,
# 그 값을 포함하는 새로운 리스트 생성
name_list = ["철수", "훈이", "유리", "흰둥이", "수지"]
selected_name = [name for name in name_list if "수" in name]
print(selected_name)
# 예시4: [1,2,3,4,5]에서 3보다 큰 숫자들의 제곱을
# 포함하는 새로운 리스트 생성
print([x**2 for x in [1, 2, 3, 4, 5] if x > 3])
