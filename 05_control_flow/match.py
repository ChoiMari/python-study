# match문(Python 3.10+)
# Python 3.10부터 조건문을 보다 강력하게 표현 가능한
# match 문법 새롭게 추가됨
# 패턴 매칭 개념을 기반으로,
# 다양한 조건을 보다 간결하고, 직관적으로
# 표현할 수 있는 문법
# 기존의 if-elif-else 문과 유사하지만,
# 단순한 조건 비교를 넘어서 구조와 형태까지
# 비교할 수 있는 패턴 매칭 기능을 제공한다는 점에서 차이가 있음

# 문법
# match 비교할_값:
#     case 패턴1:
#         실행문

#     case 패턴2:
#         실행문

#     case _:
#         실행문  # 위의 어떤 case에도 해당하지 않을 때 실행

# 예시
# if-elif-else문
day = "월요일"
if day == "월요일":
    print("평일")
elif day == "화요일":
    print("평일")
elif day == "수요일":
    print("평일")
elif day == "목요일":
    print("평일")
elif day == "금요일":
    print("평일")
elif day == "토요일":
    print("휴일")
elif day == "일요일":
    print("휴일")
else:
    print("알 수 없는 요일")

# -----------------------------------
# match문
match day:
    case "월요일":
        print("평일")
    case "화요일":
        print("평일")
    case "수요일":
        print("평일")
    case "목요일":
        print("평일")
    case "금요일":
        print("평일")
    case "토요일":
        print("휴일")
    case "일요일":
        print("휴일")
    case _:
        print("알 수 없는 요일")

# --------------------------------------
# match-case 전용 OR 패턴 문법
# case 패턴 사이에는 or을 못씀(문법 오류)
# | 를 사용하도록 정해져 있다

# (일반 python에선 | 쓰면 비트연산)
# match-case에는 and 패턴 없음
# and 조건 필요 시 if 사용
day = "일요일"
match day:
    case "월요일" | "화요일" | "수요일" | "목요일" | "금요일":
        print("평일")
    case "토요일" | "일요일":
        print("휴일")
    case _:
        print("알 수 없는 요일")
