# 문자열 자료형
name = "홍길동"
print(type(name))  # <class 'str'>

fruit1 = "딱복"
fruit2 = "물복"
print(fruit1, fruit2, sep="-")

str1 = "I'm hong"
# 작은 따옴표를 넣으려면 큰따옴표로 감싼다
print(str1)

# 이스케이프 시퀀스(\) 사용도 가능
# str2 = 'He\'s'
# print(str2) He's

# 여러줄 문자열
str3 = """
여
러
줄
문자열
"""
print(str3)  # 줄바꿈 그대로 출력됨
# 여
# 러
# 줄
# 문자열

# 붙이고 싶으면?
str4 = """\
여\
러\
줄 \
문자열
"""

print(str4)  # 여러줄 문자열
