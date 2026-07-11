# 객체
# 클래스를 사용하여 만들어진 값을 객체라고 한다

# 인스턴스
# 클래스를 사용하여 만들어진 객체를 인스턴스
# 객체 관계 위주로 설명할 때 사용하는 용어

# 속성
# 인스턴스 변수: 각 인스턴스마다 별도로 존재하는 변수
# 클래스 변수: 클래스의 모든 인스턴스가 공유하는 변수

# 메서드
# 인스턴스 메서드: 각 인스턴스마다 별도로 존재하는 메서드
# 클래스 메서드: 클래스의 모든 인스턴스가 공유하는 메서드
# 정적 메서드: 클래스 안에 정의 되어있지만,
#   인스턴스(self)나 클래스와는 관련 없이 독립적으로 동작하는 메서드


class Student:
    school_name = "떡잎초"  # 클래스 변수
    # 클래스 전체가 공유하는 값

    def __init__(self, name):
        # 인스턴스 변수, 속성
        # 객체를 만들 때마다 각 객체 내부에 따로 생성됨
        self.name = name

    # 인스턴스 메서드
    def study(self) -> None:
        print(f"{self.name}은 공부한다.")

    # 클래스 메서드: 클래스를 가리키는 값(cls)을 첫번째 파라미터로 받아야함
    @classmethod  # 데코레이터 지정해야함
    def change_school_name(cls, new_school_name: str) -> None:
        cls.school_name = new_school_name

    @classmethod
    def get_school_name(cls):
        return cls.school_name

    # 정적 메서드: 첫번째 매개변수로 반드시 전달 받아야할 값없음
    @staticmethod  # 호출 시엔 클래스명으로 접근하는것을 권장
    def is_valid_name(name: str) -> bool:
        """두글자 이상이면 True, 미만이면 False를 반환"""
        return len(name) >= 2

    # 인스턴스가 필요없는 기능이라는 것을 명확하게 하기 위해..
    # self가 굳이 필요 없다면..(객체 상태를 사용하지 않음)
    # 기능 별로 묶기 위해서


# 인스턴스 메서드: 특정 객체의 데이터(상태) 다룸,
#    첫번째 파라미터 self
# 클래스 메서드: 클래스 전체의 공통 데이터(동작)
#    첫번재 파라미터 cls

# (관례) 객체.메서드() -> 인스턴스메서드, self 객체 1개
#       클래스명.메서드() -> 클래스메서드 또는 정적 메서드, cls 클래스 전체

# <메모리>
# Student 클래스
# └─ school_name = "떡잎초"   ← 클래스 변수 1개, 공유

# student1 객체
# └─ name = "철수"

# student2 객체
# └─ name = "유리"

stu1 = Student("철수")
stu2 = Student("유리")
print(stu1.school_name)  # 떡잎초
print(stu2.school_name)  # 떡잎초

# 클래스 변수를 대입해서 바꾸는 경우?
# 해당 객체만 바꾸는 것
stu1.school_name = "떡잎유치원"
print(stu1.school_name)  # 떡잎유치원
print(stu2.school_name)  # 떡잎초

# 진짜 클래스 변수 값을 바꾸려면 클래스명으로 접근
Student.school_name = "떡잎유치원"
print(stu2.school_name)  # 떡잎유치원

# 실제 클래스 변수에 접근할 땐
# 클래스 이름으로 접근하는 것을 권장한다고 함


# 클래스메서드 호출?
# 인스턴스로 접근, 클래스이름으로 접근 둘 다 되지만
# 클래스이름으로 접근을 권장함
Student.change_school_name("떡볶이 학교")
print(Student.get_school_name())

print(Student.is_valid_name(stu1.name))  # True
