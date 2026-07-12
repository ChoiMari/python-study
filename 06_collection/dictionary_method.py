# 딕셔너리 메서드
my_dict = {"a": 1, "b": 2, "c": 3}

# 조회관련
# keys():딕셔너리의 모든 키를 반환
print(my_dict.keys())  # dict_keys(['a', 'b', 'c'])
# dict_keys라는 객체가 출력됨, list자료형과 다르다고
# 반복문 사용 시 더 활용된다고 함

# values(): 딕셔너리의 모든 값을 반환
print(my_dict.values())  # dict_values([1, 2, 3])

# items(): 딕셔너리의 모든 키-값을 반환
print(my_dict.items())  # dict_items([('a', 1), ('b', 2), ('c', 3)])

# get(key, default=None): 키에 해당하는 값을 반환,
#   키가 존재하지 않으면 default 값을 반환함
print(my_dict.get("a"))  # 1
print(my_dict.get("d"))  # None

# print(my_dict.get("d", default="없음"))
# TypeError: dict.get() takes no keyword arguments
# dict.get()은 Python으로 작성된 함수 아니고
# CPython(C언어)로 구현된 내장메서드라서 위치 아규먼트만 받도록 설계됨
# default= 이런 키워드 인자로 할당 못씀
print(my_dict.get("d", "해당 키 없음"))  # 해당 키 없음

# in 연산자 : 특정 키가 딕셔너리에 존재하는 지 확인함
print("b" in my_dict)  # 키 "b"가 my_dict에 존재하는지 확인
# True
print("z" in my_dict)  # False

# 수정 관련
# update(other_dict): 다른 딕셔너리의 키-값 쌍을
#   현재 딕셔너리에 추가하거나 업데이트함
my_dict = {"가": 1, "나": 2}
other_dict = {"다": 3}
my_dict.update(other_dict)
print(my_dict)  # {'가': 1, '나': 2, '다': 3}
# 중복 키가 있다면 덮어쓴다

# setdefault(key, default=None): 키가 딕셔너리에 존재하지 않으면
#   해당 key와 default로 설정한값을 value값으로 추가하고 반환함
#   키가 이미 존재하면 해당 키의 값을 반환함
print(my_dict.setdefault("다"))  # 3
print(my_dict.setdefault("라", "4"))  # 4
# "라"라는 키가 없어서
# "라"라는 키를 설정한 4를 value로 저장해서 새롭게 추가하고 반환됨
print(my_dict)  # {'가': 1, '나': 2, '다': 3, '라': '4'}
# 이미 기존에 있는키었다면 기존 value값 반환

# 삭제관련
# pop(key, default=None): 키에 해당하는 값을 제거하고 반환
#   키가 존재하지 않으면 default 값을 반환함
my_dict = {"가": 1, "나": 2, "다": 3}
print(my_dict.pop("나"))  # 2
print(my_dict)  # {'가': 1, '다': 3}
print(my_dict.pop("라", "해당 키 없음"))  # 해당 키 없음
# 키없을 시, default 지정 안하면 KeyError발생
# print(my_dict.pop("라"))  # KeyError: '라'

# popitem(): 딕셔너리에서 마지막의 키-값 쌍을 제거하고 반환함
# 반환 타입은 튜플(tuple)
# 딕셔너리가 비어 있으면 KeyError가 발생
print(my_dict.popitem())  # ('다', 3)
print(my_dict)  # {'가': 1}

# clear(): 딕셔너리의 모든 키-값 쌍을 제거함
my_dict = {"가": 1, "나": 2, "다": 3}
my_dict.clear()
print(my_dict)  # {}

# 기타 유틸리티
# copy(): 딕셔너리의 **얇은** 복사본을 반환함
# 깊은 복사는 못함
my_dict = {"가": 1, "나": 2, "다": 3}
other_dict = my_dict  # 같은 참조, 메모리 같은 곳을 바라봄
print(my_dict)
my_dict["라"] = 4
print(other_dict)  # {'가': 1, '나': 2, '다': 3, '라': 4}

other_dict = my_dict.copy()  # 같은 참조 공유하지 않음
my_dict.pop("라")
print(my_dict)  # {'가': 1, '나': 2, '다': 3}
print(other_dict)  # {'가': 1, '나': 2, '다': 3, '라': 4}
# 이렇게 얕은 복사는 가능
# 하지만 내부의 리스트, 딕셔너리 같은 참조 객체는 공유
my_dict["라"] = {"r": 10}
other_dict = my_dict.copy()
print(my_dict)  # {'가': 1, '나': 2, '다': 3, '라': {'r': 10}}
my_dict["라"]["r"] = 30
print(other_dict)  # {'가': 1, '나': 2, '다': 3, '라': {'r': 30}}
# 깊은 복사가 필요하면 copy.deepcopy()를 사용

# fromkeys(iterable, value=None): 키 여러 개를 한 번에 만들고, 값을 모두 똑같이 넣는 함수
# 주어진 iterable의 요소를 키로하고 value를 값으로 하는 새로운 딕셔너리를 생성
# iterable: 반복할 수 있는 객체(for문에서 사용할 수 있으면..)
#   list, tuple, str, range, dictionary, set 등
keys = ["a", "b", "c"]
new_dict = dict.fromkeys(keys, 1)
print(new_dict)  # {'a': 1, 'b': 1, 'c': 1}

# len(): 딕셔너리의 키-값 쌍의 개수를 반환
print(len(new_dict))  # 3

# 딕셔너리 추가
# dict[key] = value
# dict.update(other_dict)
# dict.setdefault("key", defaultvalue)
