#실습 - 금융가 룰렛
# 금융가 직원들은 계산을 할 때,
# 모두가 명함을 꺼내서 그릇에 넣는다고 함
# 부유한 은행가들이 하는 러시안 룰렛 같은 게임이 있다고..
# 뽑힌 명함의 주인이 일행의 계산서를 모두 지불.

# random모듈과 List를 이용해서 구현.
# list에 있는 이름들 중 하나를 무작위로 출력하는 코드를 작성해보자
# 코드를 실행할 때마다 다른 이름들이 출력.
import random

friends = ["Jiwoo", "Minjun", "Suyeon", "Minji", "Jihoon"]

# 방법 1
#random.choice() : 리스트에서 무작위로 한 개를 뽑아 반환
print(random.choice(friends))

# 방법 2
random_number_int: int = random.randint(0, len(friends) - 1) 
# 0이상 friend list의 길이 -1 이하의 랜덤한 정수 반환
# 인덱스는 0부터 시작하므로 -1해야 갯수가 맞음
print(friends[random_number_int])