#[참고 지식]
# sep(searator): print()함수에서 출력할 값들
# 사이에 들어가는 구분자를 지정하는 키워드 
# 기본값은 공백 한 칸 " "
# 여러 값을 출력 할 때 값과 값 사이에 어떤 문자를 넣을지 정하는 용도
print("사과", "바나나", "체리")  
# 출력: 사과 바나나 체리  (기본 공백)

print("사과", "바나나", "체리", sep=", ")  
# 출력: 사과, 바나나, 체리

print("2023", "08", "12", sep="-")  
# 출력: 2023-08-12

#실무에서 출력 포맷 조정, 로그 작성, CSV 생성 등 다양한 곳에서 아주 자주 쓰인다!!

# print()가 기본적으로 출력 후에 자동으로 한다

#end 
# end는 그 기본 줄바꿈을 다른 문자열로 바꾸거나 없앨 때 사용함
print("Hello", end=" ")  
print("World")  
# 출력: Hello World  (줄바꿈 대신 공백으로 연결)

print("안녕하세요", end="!!\n")  
print("파이썬")  
# 출력: 안녕하세요!!
#       파이썬


# 표준 입출력
import sys # 파이썬 시스템 관련 기능을 모아둔 모듈
# 표준 입출력, 명령행 인자, 등 다양한 시스템 기능 제공

# sys.stdout
#표준 출력 스트림, 콘솔 화면으로 출력이 나가는 대상

# sys.stderr 표준 에러 스트림
# 에러 메세지, 경고, 로그 등 오류 관련 출력 전용 스트림
# 에러메세지만 따로 파일로 저장하고 싶을 때 별도로 관리 가능?

print("메시지")
# 내부적으로는 file=sys.stdout이 기본값이라 표준 출력(stdout)으로 나간다!
#  print("메시지") == print("메시지", file=sys.stdout)
# 굳이 file=sys.stdout을 안 써도 동작은 똑같음

#print(..., file=sys.stderr)
# 표준 에러(stderr) 로 출력
#화면에는 똑같이 보이지만, 출력 스트림이 다르기 때문에 리디렉션이나 로그 분리에서 차이가 발생

# 왜 사용?
# CLI 도구, 서버 로그, 데이터 처리 파이프라인에서
# 정상 데이터는 stdout
# 오류 메시지는 stderr
# 로 구분해서 보내야 다른 프로그램이 결과만 깔끔하게 받을 수 있음

#python test.py > out.txt 2> err.txt
# stdout 출력은 out.txt에 저장
# stderr 출력은 err.txt에 저장

#시험 성적
scores = {"수학": 100 , "영어": 98, "코딩": 100}
for subject, score in scores.items() :
    print(subject.ljust(8), str(str).ljust(4))
