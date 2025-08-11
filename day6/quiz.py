# 퀴즈
# 표준 체중을 구하는 프로그램을 작성하시오

#[참고] 파이썬에서는 코드가 길어질 때 ()로 묶어서 줄바꿈 가능
def std_weight(height:float, gender:str) -> float :
    if (gender == "남자" 
        or gender.upper() == "M" 
        or gender.lower() == "man") :
       return round(height * height * 22, 2)
    elif (gender == "여자" 
          or gender.upper() == "W" 
          or gender.lower() == "woman") :
        return round(height * height * 21, 2)
    else :
        raise ValueError(f"잘못된 입력: {gender}") # 예외 던짐

height = 175
gender = "남자"
# :.1f 포맷지정자(소수점 1자리수로 출력)
print(f"키 {height}cm {gender}의 " 
      f"표준 체중은 {std_weight(height / 100, gender)}kg 입니다.")

