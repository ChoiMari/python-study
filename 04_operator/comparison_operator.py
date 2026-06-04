# 비교 연산자
# 피연산자를 비교하여 True, False를 반환하는 연산자
# == 같다
print(1 == 1)  # True
# != 같지 않다
print(1 != 1)  # False
# 크다 >
print(2 > 1)  # True
# 작다 <
print(4 < 10)  # True
# 크거나 같다 >=
print(5 >= 5)  # True
# 작거나 같다 <=
print(1 <= 10)  # True

# 파이썬의 비교 연산자 특징
# 문자도 크고 작음 비교 가능
# 문자열 비교는 유니코드 값을 기준으로
# **앞에서부터 비교**한
# ord()함수를 사용하여 문자의 유니코드 값을 확인 가능
print(ord("a"))  # 97
print(ord("A"))  # 65

print("A" > "a")  # Flase
print("a" < "z")  # True

print("apple" > "apz")  # False
# 앞에서 부터 비교, p와 z에서 z가 더 크기때문에 False
print("abc" < "abcd")  # True 뒤의 글자가 더 많은게 크다
# 연속 비교가 가능
# a < b < c
if 1 < 2 < 3:
    print("통과")

print(1 == 1 != 8)  # True
