#List

korea = ["Seoul", "Busan", "Incheon", "Deagu", "Daejeon", "Gwangju", "Ulsan"]

# index로 접근 가능
# 파이썬은 양의 인덱스, 음의 인덱스가 존재함
# 양의 인덱스는 0부터 시작(리스트의 맨 처음 아이템을 가리킴)
# 음의 인덱스는 -1부터 시작(리스트의 맨 마지막 아이템을 가리킴)
print(korea[0]) #Seoul
print(korea[-1]) #Ulsan


#리스트 값 변경하기(index이용)
korea[1] = "Gangneung" 
#리스트 korea의 인덱스 1번에 저장된 값이 부산에서 강릉으로 변경됨
print(korea) 

# append()함수로 아이템 추가 가능(리스트 끝에 단일 항목으로 추가됨)
korea.append("Jeju")
print(korea)

# extend() : 기존 리스트 위에 다른 리스트의 모든 원소를 한꺼번에 추가함
korea.extend(["Suwon", "Gumi"])
print(korea) 

# 더 많은 함수는 파이썬 공식 문서에서 확인 가능.
# https://docs.python.org/3/tutorial/datastructures.html

