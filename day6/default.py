# def profile(name:str, age:int, lang:str) -> None :
    # print(f"이름 : {name}, 나이 : {age}, 언어: {lang}")

# 나이와 언어가 다 같은 경우??
# 같은 값을 다 일일이 넣어서 호출하기 불편
# 기본값 설정!

def profile(name:str, age:int = 18, lang:str = "Java") -> None :
    print("이름 : {}, 나이 : {}, 언어 : {}".format(name, age, lang))

profile("홍길동")
profile("임꺽정")
