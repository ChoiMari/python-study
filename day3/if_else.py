# if/else 구문
# if 조건:
#   실행문1
# else:
#   실행문2
# 주의) 들여쓰기를 잘해야함
print("롤러코스터를 타러 오신 여러분을 환영합니다!")
height = int(input("당신의 키는 몇 cm인가요?"))

if height > 120:
    print("당신은 롤러코스터를 탈 수 있습니다!")
else:
    print("죄송하지만, 키가 좀 더 자라면 탈 수 있겠습니다.")