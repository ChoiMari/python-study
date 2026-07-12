# 모듈이란?
# 모듈: 다른 코드에서 불러와서 사용할 수 있는 기능 단위를 의미
# 파이썬에서 .py 확장자로 끝나는 파일은 모듈로 취급된다
# 즉 파이썬에서는 .py 파일 하나하나가 재사용 가능한 코드묶음
# 모듈 안에 작성된 함수, 변수, 클래스 등을
# 다른 파일에서 가져다 사용할 수 있다.
import calculator as calc

# import문 사용해서 다른 파일에서 불러와 사용가능
# 모듈 이름이 곧 파일 이름
# calculator.py에 작성되어 있는 함수, 변수, 클래스 등
# 가져다 쓰겠다
# 파이썬에서 이게 가능한 이유는
# 파이썬 프로그램이 .py파일 하나하나를 모듈로 취급하기 때문
# 하나하나의 .py 파일을 재사용 자능한 부품으로 생각
# import
# 다른 모듈(파일)의 코드(함수, 변수, 클래스 등)를 현재 파일에서 사용하기 위해 가져오는 문법이다.
#
# calculator
# -> calculator.py 파일(모듈)을 의미한다.
#
# as calc
# -> calculator라는 이름 대신 calc라는 별칭(alias)으로 사용하겠다는 의미이다.
#
# 즉,
# calc.add()
# 는
# calculator.add()
# 와 동일하다.
result1 = calc.add(1, 2)
result2 = calc.minus(13, 2)
print("Addition:", result1)
print("Subtraction:", result2)

# Java: 패키지명.으로 접근해서 클래스를 import
# 파일(모듈)을 import

# 파이썬에는 모듈이 여러 종류가 있음
# .py파일
# Python 라이브러리
# install(설치)한 외부 라이브러리
# 라이브러리 = 모듈들의 집합
