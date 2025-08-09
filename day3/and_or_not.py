print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

# 45세 ~ 55세 중년의 위기를 겪고 있는 이들에게 입장권을 무료로 나눠주기로 함
# 논리연산자를 사용해서 코드 작성을 해보자.
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55: # 파이썬에서는 &&를 사용하지 않으며, 45 <= age <= 55로 쓸 수도 있음
        # bill = 0 생략 가능
        print("축하합니다! 당신을 위한 특별한 무료 요금입니다 ^__^ 즐겁게 이용하세요!")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")
