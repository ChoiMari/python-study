# 딕셔너리(dictionary)
# 키:값 쌍으로 데이터를 저장하는 자료형
# 중괄호 {}를 사용하여 정의, 키와 값은 : 콜론으로 구분함
# 키는 고유(중복 X), 값은 중복 가능
# 키 중복 사용하면 덮어씀(결국 1개만 생성되는 것)

# 딕셔너리 예시
my_dict = {"과일": ["포도", "복숭아", "'딸기"], "name": "길똥", "age": 22}
print(type(my_dict))  # <class 'dict'>
print(my_dict)  # {'과일': ['포도', '복숭아', "'딸기"], 'name': '길똥', 'age': 22}

# 키로 값 접근
print(my_dict["과일"])  # ['포도', '복숭아', "'딸기"]
print(my_dict["age"])  # 22

# 수정 : 변수 사용하듯이 키로 접근해서 재할당 하면 됨
my_dict["과일"] = "납작복숭아"
print(my_dict["과일"])  # 납작복숭아

# 추가
my_dict["city"] = "서울"
print(my_dict["city"])  # 서울
print(my_dict)

# 삭제: 이미 존재하고 있는 딕셔너리의 키와 값 삭제하고 싶을 때
# del 키워드 사용
del my_dict["과일"]
print(my_dict)  # {'name': '길똥', 'age': 22, 'city': '서울'}
# print(my_dict["과일"])  # KeyError: '과일'
