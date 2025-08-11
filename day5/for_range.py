#for문과 range()함수

# start : 1
# stop : 10
# step : 1(기본값)
for number in range(1, 10): #1부터 1씩 증가하며 10되면 멈춤(10이 되면 반복 안함)
    print(number) # 1~9까지 출력됨

# The Gauss Challenge
# 1~100까지 더하기
result : int = 0 # 합계를 저장할 변수 초기화
for number in range(1, 101): # 1부터 1씩 증가하며 101되면 멈춤(즉, 100까지 반복실행)
    result += number
print(result) # 5050

