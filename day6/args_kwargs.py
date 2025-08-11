# 가변 인자
#def profile(name:str, age:int, *lang:str) -> None :
#    print(f"이름 : {name}, 나이 : {age}")
#    print(f"언어 : {lang}")

print("문장 이어서 출력 ", end = " ")
print("이어서 출력 이어서 출력")


# 출력 시 튜플 형태가 아닌 깔끔한 문자열로 보려면?
# join()사용
def profile(name:str, age:int, *lang:str) -> None :
    print(f"이름 : {name}, 나이 : {age}", end = " ")
    print(f"언어 : {', '.join(lang)}")

profile("임꺽정", 22, "C")
profile("홍길동", 70, "Java", "C", "C++")
profile("춘향이", 22, "C", "C#", "JavaScript", "Java")

