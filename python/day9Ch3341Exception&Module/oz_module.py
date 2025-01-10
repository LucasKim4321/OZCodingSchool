# oz_module.py

# 원주율 값을 변수 p1에 저장합니다.
p1 = 3.141592

# 사용자로부터 반지름 값을 입력받는 함수입니다.
def number_input():
    value = input("반지름을 입력해주세요")
    return float(value)

# 반지름을 입력받아 원의 둘레를 계산하는 함수입니다.
def get_circum(radius):
    # 원의 둘레 계산 공식: 2 * π * 반지름
    return 2 * p1 * radius

# 반지름을 입력받아 원의 넓이를 계산하는 함수입니다.
def get_circle(radius):
    # 원의 넓이 계산 공식: π * 반지름^2
    return p1 * radius * radius