# 클래스(class)
# 데이터와 그 데이터를 처리하는 함수(메서드)를
# 하나로 묶어 놓은 설계도 같은 개념
# 클래스를 사용하면 데이터(상태,필드)와 동작(메서드)을
# 함께 가지는 객체(object)를 쉽게 생성할 수 있다.

# 클래스 정의
# class 클래스명:
#       클래스의 내용

# class 키워드 이용하여 정의함
# 클래스명은 파스칼 케이스 규칙을 따름
# 파스칼케이스: 각 단어의 첫글자를 대문자로 시작함


class Calculator:
    # 클래스 내부 데이터(상태) 정의할 땐 __init__ 메서드사용
    def __init__(self, name: str):  # 해당 클래스 호출 시 자동으로 호출됨
        # 속성
        self.name = name  # 자동으로 인스턴스 필드 생성됨

    # 메서드 : 클래스 안에 정의된 함수
    def add(self, x: int, y: int) -> int:
        print(f"{self.name} 더하기 실행")
        return x + y

    # 클래스 내부의 메서드는 반드시
    # 첫번째 파라미터로 self 지정해야 함
    # self: 클래스 자기 자신을 가리킴


claculator = Calculator("일반계산기")  # 클래스 호출 하면
# 내부 동작
# Calculator.__new__() 객체를 메모리에 생성
# Calculator.__init__() 필드 초기화

print(type(claculator))  # <class '__main__.Calculator'>
print(claculator)  # <__main__.Calculator object at 0x0000018788FA6390>

print(claculator.add(1, 2))
print(claculator.name)
