# 상속
# 기존에 정의된 클래스의 속성과 메서드를 그대로 물려받아.
# 새로운 클래스를 만드는 것을 의미함
# 부모 클래스의 속성,메서드를 자식 클래스가
# 물려받아 재사용 가능


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


class Child(Parent):
    pass


print(Child.class_var)
child = Child()
print(child.intance_var)
child.instance_method()
Child.class_method()
Child.static_method()
