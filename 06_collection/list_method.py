# 리스트메서드
# 메서드란 특정 자료형에 미리 내장된 함수를 말함

list1 = [1, 2, 3]
# 데이터 추가
# append(): 리스트의 끝에 요소 추가
list1.append(4)  # 한번에 1개의 데이터만 추가 가능
print(list1)  # [1, 2, 3, 4]

list2 = [10, 11, 12]
list1.append(list2)
print(list1)  # [1, 2, 3, 4, [10, 11, 12]]

# insert(index, value): 리스트의 특정 위치에 요소 추가
list1.insert(0, 7)  # [7, 1, 2, 3, 4, [10, 11, 12]]
# 0번 인덱스에 7추가
print(list1)

list3 = [5, 6]
# extend(): 다른 리스트의 요소를 현재 리스트에 추가
list2.extend(list3)
print(list2)  # [10, 11, 12, 5, 6] 기본 리스트에 병합됨

# 데이터 삭제
# remove(value): 리스트에서 특정 값을 제거하는 메서드
# 요소 값으로 지우기
list1 = ["가", "나", "다", "라"]
list1.remove("나")
print(list1)  # ['가', '다', '라']

# list1.remove("하")
# ValueError: list.remove(x): x not in list
# 존재하지 않는 요소 제거 시도 시 에러 발생

# del 키워드: 인덱스로 접근한 뒤 삭제
del list1[0]  # 인덱스 0번 요소 인 '가' 삭제
print(list1)  # ['다', '라']

list2 = [0, 1, 2, 3, 4, 5]
# pop(): 인덱스 미지정 시 가장 마지막 값을 제거한 뒤 반환
print(list2.pop())  # 5
# 가장 마지막 요소 5를 제거한 뒤에 반환
print(list2)  # [0, 1, 2, 3, 4]

# pop(index): 인덱스 지정 시 그 위치의 값을 제거후 반환
print(list2.pop(1))  # 1
# 1번 인덱스의 요소를 제거한 뒤 반환
print(list2)  # [0, 2, 3, 4]

# clear(): 리스트의 모든 요소 제거 메서드
list2.clear()
print(list2)  # []

# 정보조회 및 집계
# count(value): 리스트에서 특정 값의 개수를 셈
list3 = [1, 2, 2, 3, 3, 3, 3, 3, 4]
print(list3.count(3))  # 5
# 3인 요소가 총 5번 들어있음을 반환
bool_list = [True, True, False]
print(bool_list.count(True))  # 2
# 리스트에 True가 2번 등장

# index(value): 리스트에서 특정 값의 첫 번째 인덱스 반환
print(bool_list.index(True))  # 0
# 값으로 인덱스번호를 찾는데
# True가 인덱스 0번째에 처음 등장하므로 0반환
fruits = ["사과", "바나나", "포도", "사과", "포도"]
print(fruits.index("포도"))  # 2

# print(fruits.index("복숭아"))
# ValueError: '복숭아' is not in list
# 리스트에 없는 인덱스를 찾으려하면 에러 발생

# len():리스트 길이 반환
print(len(fruits))  # 5

list1 = [100, 50, 1, 32, 11]
# 정렬 및 변형
# sort(): 요소를 오름차순으로 정렬(원본 수정)
list1.sort()
print(list1)  # [1, 11, 32, 50, 100]

fruits.sort()
print(fruits)  # ['바나나', '사과', '사과', '포도', '포도']

# 내림차순 정렬하고 싶다면?
list1.sort(reverse=True)
print(list1)  # [100, 50, 32, 11, 1]

# 특정 기준 정렬하고 싶다면? key
words = ["z", "abc", "aaaa", "sssssssss"]
words.sort(key=len, reverse=True)
print(words)  # ['sssssssss', 'aaaa', 'abc', 'z']
# 리스트 요소를 길이 기준 내림차순으로 정렬함

list2 = [4, 7, 2, 1000, 1, 500]
# reverse(): 요소를 역순으로 정렬
list2.reverse()
print(list2)  # [500, 1, 1000, 2, 7, 4]

# 원본은 냅두고 복사본 만들어서 저장하고 싶다면?
new_list2 = sorted(list2)
print(new_list2)
# [1, 2, 4, 7, 500, 1000]
# 원본은 냅두고 복사본 오름차순 정렬 후 반환

# copy(): 얕은 복사본을 만듬
# = 대입 연산자를 쓰면 같은 참조를 바라보기 때문에
# 원본까지 바뀜
list2_clone = list2.copy()
list2_clone.append("복사복사")
print(f"원본:{list2}, 복사본:{list2_clone}")
# 원본:[500, 1, 1000, 2, 7, 4], 복사본:[500, 1, 1000, 2, 7, 4, '복사복사']

# 근데 왜 얕은 복사라고 하느냐,,
matrix = [1, 2, [3, 4]]
matrix_clone = matrix.copy()
matrix_clone[2][0] = 99
print(f"원본: {matrix}")  # 원본: [1, 2, [99, 4]]
print(f"복사본: {matrix_clone}")  # 복사본: [1, 2, [99, 4]]
# 이렇게 원본까지 바뀌어버림,,
# 파이썬의 copy()는 1차 구조만 새로 복사함
# 내부 리스트까지는 복사 못하고, 내부 리스트의
# 메모리 참조 그대로 복사되었기 때문

# 깊은 복사 원한다면?
# copy모듈의 deepcopy()사용
# import copy
# 파이썬 내장 표준 라이브러리라서 존재함
# 외부라이브러리는 install 하거나 .py파일 있어야함
# matrix_deep = copy.deepcopy(matrix)
# 내부 리스트까지 새로 복사함
