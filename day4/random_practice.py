import random # random 모듈 import
# import my_module

rand_num_int = random.randint(1, 10) # 1이상 10이하의 난수 반환
print(rand_num_int)

# print(my_module.my_favorite_number)

random_num_0_to_1 = random.random() # 0.0이상 1.0미만의 실수형 난수 반환
print(random_num_0_to_1)

# random.random()을 확장해서 사용하기
random_num_0_to_10 = random.random() * 10 
# 0.0 이상 10.0미만의 실수형 난수 반환
print(random_num_0_to_10)

random_float = random.uniform(1,10) 
# 1.0이상 10.0**이하**의 실수형 난수 반환
print(random_float)