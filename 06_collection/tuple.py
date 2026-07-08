# 튜플
# 튜플은 여러 개의 데이터를 하나로 묶어서 관리할 수 있는
# 자료형을 말한다.
# 튜플은 리스트와 유사하지만, 한 번 생성된 튜플의 요소는
# **변경할 수 없는 불변한 자료형**이다.
# 튜플은 소괄호 ()로 감싸서 표현하며, 각 요소는 쉼표로 구분된다
# 튜플은 다양한 데이터 타입을 포함할 수 있으며,
# 중첩된 튜플도 가능하다.
# 튜플의 예시
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)  # (1, 2, 3, 4, 5)
print(type(my_tuple))  # <class 'tuple'>

# 튜플의 요소에 접근하기
print(my_tuple[0])  # 1
print(my_tuple[-1])  # 5

# 튜플 중첩
my_tuple2 = (1, 2, (3, 4))
print(my_tuple2)  # (1, 2, (3, 4))
print(my_tuple2[2])  # (3, 4)
print(my_tuple2[2][1])  # 4

# 튜플 슬라이싱
# [start:stop:step]
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0:4:2])  # (1,3)
print(my_tuple[:2])  # (1,2)
print(my_tuple[3:])  # (4,5)
print(my_tuple[:])  # (1,2,3,4,5)
# 행:열(직전까지)

# 튜플의 불변성
# 튜플은 불변한 자료형이므로, 한 번 생성된 튜플의 요소는 변경할 수 없다
my_tuple = (0, 1, 2, 3)
# my_tuple[0] = (1,)
# TypeError: 'tuple' object does not support item assignment
# 튜플 자료형은 요소 값 할당(수정) 지원하지 않는다
# 튜플을 불변 자료형이라서 요소 추가, 요소 수정, 요소 삭제 불가

# 튜플은 그래서 메서드도 제한적.
# 튜플의 메서드는 count()와 index()뿐이다.
# count() 메서드는 튜플에서 특정 값의 개수를 세는 메서드
my_tuple = (2, 2, 2, 3, 3, 1)
print(my_tuple.count(3))  # 2
# my_tuple에 3요소가 몇번 들어있는지 반환

# index() 메서드는 튜플에서 특정 값의 첫 번째 인덱스를 반환하는 메서드
print(my_tuple.index(1))  # 5
# 1이 처음에 등장하는 위치 인덱스 반환
print(my_tuple.index(3))  # 3
