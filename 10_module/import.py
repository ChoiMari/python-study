# import 문을 다양하게 사용하는 방법

# 1. import 모듈명
# 모듈 전체를 가져온다.
# 함수, 변수, 클래스 등을 사용할 때는
# '모듈명.'을 붙여 접근해야 한다.
#
# 예)
# import calculator
# calculator.add()

# 2. import 모듈명 as 별칭
# 모듈에 별칭(alias)을 붙여 사용할 수 있다.
# 긴 모듈 이름을 줄이거나 코드의 가독성을 높일 때 사용한다.
#
# 예)
# import calculator as calc
# calc.add()

# 3. from 모듈명 import 불러오고싶은것의 이름
# 모듈 안에 있는 특정 함수, 변수, 클래스만 가져온다.
# 가져온 이름은 모듈명 없이 바로 사용할 수 있다.
#
# 예)
# from calculator import add, minus
# result = add(1, 2)
# 모듈명. 없이 import해온 함수이름으로 호출가능

# 4. from 모듈명 import 이름 as 별칭
# 특정 함수나 클래스에도 별칭을 붙일 수 있다.
#
# 예)
# from calculator import add as plus
# result = plus(1, 2)

# 5. from 모듈명 import *
# 모듈 안의 모든 public 요소를 현재 파일로 가져온다.
# 이름 충돌이 발생할 수 있으므로 실무에서는 거의 사용하지 않는다.
# import calculator 와의 차이점은 이건 모듈명. 으로 접근해야하지만
# from 모듈명 import * 이건 그런 모듈명. 없이 안에 있는것 바로 사용가능
# 실무에서 그래서 잘 안쓰는 것.. 마지막에 import한게 덮어쓴다고 함(이름충돌)


# <정리>
# import 모듈명 : 모듈 전체를 불러오고, 모듈명.으로 접근해서 사용
# import 모듈명 as 별칭 : 모듈에 별칭을 붙여서 사용, 별칭.으로 접근해서 사용
# from 모듈명 import 필요한요소명 : 모듈안의 필요한 요소만 선택적으로 가져와서
#   모듈명. 또는 별칭. 없이 그 자체로 바로 사용 가능
# from 모듈명 import * : 모듈의 모든 요소를 가져옴(주의 필요)
