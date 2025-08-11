# 반복문 - for
fruits = ["Apple", "Peach", "Pear"]

for fruite in fruits: #리스트에 다음 요소가 없으면 종료됨
    print(fruite)
    print(fruite + " pie")
# 파이썬은 들여쓰기 레벨로 실행범위를 구분함(보통 스페이스 4칸)
# fruits의 요소 한개씩 순서대로 fruite에 담아서 반복실행되다가

# 구분
# for item in list_of_items: 
#   반복실행할_코드

#for 변수 in iterable:
#    반복 실행할 코드

# iterable에서 요소 하나씩 꺼내 변수에 할당 -> 반복 실행
# 꺼낼 요소 없으면 종료
# 여기서 in은 반복문의 키워드로 쓰임
# 멤버 연산자 in이라기 보다는 
# in은 반복할 대상을 지정하는 구문(keyword) 역할.
# 반복 대상 명시용으로 쓰임.

