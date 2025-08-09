# random 모듈을 이용한 동전 앞뒷면 출력하기
import random

random_number_int: int = random.randint(0, 1)

if random_number_int == 0:
    print("앞면입니다.")
else:
    print("뒷면입니다.")
