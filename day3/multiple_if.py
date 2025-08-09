#다중 연속 if문
#롤러코스터 타고 사진도 사갈건지?

bill = 0 # 청구서

print("롤러코스터를 타러 오신 여러분을 환영합니다!")
height = int(input("당신의 키는 몇 cm인가요? "))
age = int(input("나이가 어떻게 되시나요? "))

if height > 120:
    print("당신은 롤러코스터를 탈 수 있습니다!")
    if age < 12 :
        bill = 5
    elif age <= 18 :
        bill = 7 
    else:
        bill = 12
    wants_photo = input("사진을 사가실 건가요? 원하시면 Y 원치 않으시면 N를 입력하세요. \n")
    if wants_photo == "Y" :
        bill += 3
        print(f"총 이용 금액은 ${bill}입니다.")
    else :
        print(f"총 이용 금액은 ${bill}입니다.")
else:
    print("죄송하지만, 키가 좀 더 자라면 탈 수 있겠습니다.")