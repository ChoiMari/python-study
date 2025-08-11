# 키워드 값을 이용한 함수 호출
def profile(name:str, age:int, lang:str) -> None :
    print(f"이름 : {name}, 나이 : {age}, 언어 : {lang}")

# 키워드 아규먼트(keyword arguments) 사용 예시
# 함수 호출 시 파라미터 이름을 직접 지정
#파라미터 = 아규먼트 값을 직접 명시하면 순서를 바꿔서 호출이 가능함
profile(age = 22, name = "홍길동", lang = "Java")
profile(lang = "C", name = "임꺽정", age = 40)