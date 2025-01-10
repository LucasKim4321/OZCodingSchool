# main.py

# oz_module을 oz라는 이름으로 임포트합니다.
# 이 모듈은 원의 둘레와 넓이를 계산하는 함수들을 포함합니다.
import oz_module as oz

# oz 모듈의 number_input 함수를 호출하여 사용자로부터 반지름 값을 입력받습니다.
radius = oz.number_input()

# oz 모듈의 get_circum 함수를 호출하여 원의 둘레를 계산하고 출력합니다.
print(oz.get_circum(radius))

# oz 모듈의 get_circle 함수를 호출하여 원의 넓이를 계산하고 출력합니다.
print(oz.get_circle(radius))