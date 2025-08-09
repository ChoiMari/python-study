bmi = 84 / 1.65 ** 2
print(bmi) #30.85399449035813

# 정수변환
print(int(bmi)) 

#반올림
print(round(bmi)) # 31 소수점 첫째 자리수에서 반올림됨
print(round(bmi,1)) # 30.9 소수점 1째자리까지 표시됨 (소수점 둘째 자리수에서 반올림)
print(round(bmi,2)) # 30.85 소수점 2째자리까지 표시됨(소수점 셋째 자리수에서 반올림)

# 할당 연산자
score = 0
score += 1 # score = score + 1과 같음
score -= 1 # score = score - 1과 

# f-string
# 문자열과 다양한 데이터 타입을 쉽게 혼합해 사용이 가능
score = 0
height = 1.8
is_winning = True

#기존의 + 방식
print("당신의 점수는.. " + str(score) + "\n당신의 키는.. " + str(height)
      + "\n")

#f-string방식
print(f"당신의 점수는 {score} \n당신의 키는 {height}")
#문자열 ""앞에 f를 붙이고 {}안에 다른 타입값을 넣어서 사용

