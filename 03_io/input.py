# 값 입력받기
# 사용자가 키보드를 통해 값을 입력할 수 있도록 해주는 내장함수
# 사용자가 Enter를 누를 때까지 프로그램 실행이 대기됨
message = input("입력: ")
# 프롬프트 나오고 값 입력하면 변수에 할당
# Code Runner 확장 프로그램으로 실행하면
# 결과가 Output 탭에 표시되는 경우가 많음

# Output 탭은 사용자 입력(input)을 받을 수 없기 때문에
# input() 함수가 정상 동작하지 않음

# 따라서 터미널에서 직접 실행해야 함

# uv 사용 시
# uv run python input.py


# 일반 Python 사용 시
# python input.py

print(message, type(message))
# input()의 반환값(return value)은 항상 문자열(str)
# 숫자를 입력해도 문자열로 저장됨
