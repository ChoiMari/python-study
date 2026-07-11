# 상속
# 자식 클래스에서 동일한 이름의 속성이나 메서드를
# 정의 했을 때 어떤일이 발생하는지 살펴보자


class Parent:
    class_var = "클래스 변수"

    def __init__(self):
        self.intance_var = "인스턴스변수"

    def instance_method(self):
        print("인스턴스 메서드")

    @classmethod
    def class_method(cls):
        print("클래스 메서드")

    @staticmethod
    def static_method():
        print("정적 메서드")


# 권장되는 방식
# 객체. 인스턴스 변수, 인스턴스 메서드
# 클래스명. 클래스 변수, 클래스 메서드, 정적메서드


# 파이썬은 다중 상속 가능함
class Child(Parent):
    # 부모클래스와 동일한 클래스 변수 정의
    class_var = "자식 클래스 변수"

    # 부모 클래스와 동일한 인스턴스 변수 정의
    def __init__(self):
        super().__init__()  # Parent.__init__()

    # 오버라이딩
    def instance_method(self):
        print("자식 인스턴스 메서드")


child = Child()
print(Child.class_var)  # 자식 클래스 변수
# 부모클래스의 속성이 자식 클래스에 의해 가려지는 현상
# 변수 새도잉

# print(child.instance_var)  # 자식 인스턴스 변수
# AttributeError: 'Child' object has no attribute 'instance_var'
# 자식 클래스에 __init__(self)존재하면
# Child() 클래스 호출 했을 때
# 자식클래스의 Child.__init__(self)이 호출되므로
# child안에는 instance_var가 존재하지 않음

# 자식 클래스에 __init__()을 직접 정의하면
# Child() 생성 시 Parent.__init__()은 자동으로 호출되지 않는다.
# 호출되지 않았으므로
# 따라서 Parent.__init__()에서 생성하는
# 인스턴스 변수(self.instance_var)는 생성되지 않는다.
#
# 그래서 child.instance_var에 접근하면
# AttributeError가 발생한다.

# 그래서 만약, 자식 클래스에서 __init__(self)메서드를
# 정의한다면 그 안에서 super().__init__() 직접 호출해주어야함
# Python은 자동으로 추가 안해줌(명시해야함)
print(child.intance_var)  # 인스턴스변수
child.instance_method()  # 자식 인스턴스 메서드
