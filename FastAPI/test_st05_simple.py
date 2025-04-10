# pytest 사용시
# 함수 이름 앞에 test_라고 써주면 test 함수인걸 인식한다.

# 파이참에서 pytest 함수를 만들면 테스트 실행버튼이 생긴다.
# 터미널에서 테스트 실행 시 pytest . 이렇게 입력하면 됨.
def test_simple() -> None:
    print("Testing simple")

    # 0으로 무언갈 나눌 수 없기 때문에 ZeroDivisionError 오류가 난다.
    # print(1/0)

    # 에러 발생을 예상했고 거기에 따른 예외 처리도 했기 때문에 무사히 넘어갈 수 있다.
    try:
        1/0
    except ZeroDivisionError:
        print("Division by zero")

# 제품 코드
def add(a: int, b: int) -> int:
    return a + b

# 테스트 코드
def test_add() -> None:
    # Given : 재료를 준비합니다.
    # 버그는 "경계"를 좋아합니다.
    # int의 경우에는 -1, 0, 1
    a, b = 1, 2

    # When : 테스트 대상이 되는 함수를 호출합니다.
    result = add(a, b) # result의 타입은 int

    # Then :
    assert result == 3



# assert 1+1 == 3  # 에러
# assert 1+1 == 3, "계산이 틀렸습니다"  # 에러 감지시 에러문 표시