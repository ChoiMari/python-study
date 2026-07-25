# 파이썬은 모든 데이터를 객체(object)로 다루는 언어
class Parent:
    pass


pr = Parent()  # 클래스 호출
print(type(pr))  # <class '__main__.Parent'>

text = "hello"
print(type(text))  # <class 'str'>

num = 10
print(type(num))  # <class 'int'>


# 함수도 객체
def add(x, y):
    return x + y


print(type(add))  # <class 'function'>

# 객체는 속성과 메서드에 접근 가능
