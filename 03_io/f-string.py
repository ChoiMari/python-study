# f-string
# python 3.6이상에서 사용할 수 있는 문자열 포맷팅 방법
# f-string은 문자열 앞에 f를 붙이고, {}안에 변수나 값 삽입하는 방법

name = "짱구"
age = 5

#:정렬폭.정밀도f
# > 오른쪽 정렬
# ^ 가운데 정렬
# > 왼쪽 정렬
print(f"{name:>10}는 {age:^10.5f}살")
#        짱구는  5.00000  살

# f-string {}안에 계산식도 가능
print(f"{10 + 5}")  # 15

x = f"안녕? {name:^10}, {5 + age:>10}"
print(x)
# 안녕?     짱구    ,         10

# 복습(%퍼센트 포맷팅)
# %[flags][width][.precision]type
print("안녕 %-10s야. 넌 %.2f살이야" % (name, age))
# 안녕 짱구        야. 넌 5.00살이야
