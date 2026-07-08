# 함수(function)
# 특정 작업을 수행하도록 정의된 코드 블록
# 반복적으로 사용하는 코드를 함수로 만들어두면,
# 필요할 때마다 재사용하여 호출 할 수 있기 때문에
# 가독성을 높일 수 있다.
# def 키워드를 사용하여 함수 정의
# def : define 정의하다의 약자


# 함수 정의
def add(a: int, b: int) -> int:
    return a + b


# 함수 호출
print(add(1, 3))


def gugudan(x: int) -> None:
    for i in range(1, 10):
        print(f"{x} * {i} = {x * i}")


gugudan(2)


# docstring 문서 문자열
# 파이썬에서 코드의 사용법이나 역할을 설명하기 위해 작성하는 공식 주석
# 함수에서 사용할 경우, 함수의 정의 바로 아래에 작성함
# 함수 목적과 사용 방법을 설명
def subtract(x: int, y: int) -> int:
    """두 개의 정수를 아규먼트로 받아 뺄셈 계산을 하여
    그 결과를 반환하는 함수"""
    return x - y


# docsting은 함수의 __doc__ 속성으로 접근 가능함
# 큰 따옴표 3개 또는 작은 따옴표 3개로 묶어서 사용함
print(subtract.__doc__)
# 두 개의 정수를 아규먼트로 받아 뺄셈 계산을 하여
#    그 결과를 반환하는 함수
