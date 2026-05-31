# 형변환
# 어떤 값의 자료형을 다른 자료형으로 변환하는 것을 의미
# str -> int, int ->str, int -> float

# int() : 정수형 변환
num_str = "123"
num_int = int(num_str)
print(num_int, type(num_int))  # 123 <class 'int'>

# float(): 실수형으로 변환
num_str = "3.14"
num_float = float(num_str)
print(num_str, type(num_float))  # 3.14 <class 'float'>

# str(): 문자열형으로 변환
num = 1000
num_str = str(num)
print(num_str, type(num_str))  # 1000 <class 'str'>

# bool(): 논리형으로 변환
# 빈 문자열(""), 0, 0.0, None은 False,
# 나머지는 True로 변환
num_str = ""
num_bool = bool(num_str)
print(num_bool, type(num_bool))  # False <class 'bool'>

num_int = 1
num_bool = bool(num_int)
print(num_bool, type(num_bool))  # True <class 'bool'>
