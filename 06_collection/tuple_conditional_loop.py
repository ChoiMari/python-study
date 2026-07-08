# 튜플과 조건문 반복문

# 조건문
# - 튜플이 비어있는지 확인하기
# 0, 0.0, '', [], {}, set(), () 등은 모두 False로 간주됨
my_tuple = (1, 2, 3, 4, 5)
if my_tuple:
    print("튜플에 요소 있음")  # 실행
else:
    print("튜플 비어있음")

# 튜플에 특정 값이 있는지 확인
if 5 in my_tuple:
    print("튜플에 요소 5가 존재")  # 실행
else:
    print("튜플에 요소 5가 없음")

# 튜플 + 반복문
# - while 루프 사용할 수도 있지만,
# 튜플을 순회할 때는 for 루프가 일반적
my_tuple = (5, 4, 3, 2, 1)
for item in my_tuple:
    print(item, end=" ")  # 5 4 3 2 1

print()
print("=" * 50)

# 튜플 + 반복문 + 조건문
my_tuple = (1, 4, 5, 6, 9, 10)
for item in my_tuple:
    if item % 2 == 0:
        print(f"{item}: 짝수", end=", ")
    else:
        print(f"{item}: 홀수", end=", ")
print()
# 튜플 + 제너레이터 표현식
# 튜플은 컨프리헨션이 없는 대신 제너레이터 표현식을
# 사용할 수 있다.
# 제너레이터 표현식은 튜플과 유사하지만,
# 메모리를 효율적으로 사용하기 위해 값을 하나씩 생성하는 방식
# 생성된 값을 tuple() 함수를 사용하여 튜플로 변환 가능
generator_express = (x for x in range(5))
print(type(generator_express))  # <class 'generator'>

# (x for x in range(5)) 리턴값 제너레이터 타입
print(generator_express)  # <generator object <genexpr> at 0x000001D4950FCA00>
# 바로 사용 불가
# 그래서 next()라는 내장함수 이용
print(next(generator_express))  # 0
print(next(generator_express))  # 1
print(next(generator_express))  # 2
print(next(generator_express))  # 3
print(next(generator_express))  # 4

generator_express = tuple(x for x in range(5))
# 튜플 자료형으로 변환해서 사용 가능
print(type(generator_express))  # <class 'tuple'>
print(generator_express)  # (0, 1, 2, 3, 4)
