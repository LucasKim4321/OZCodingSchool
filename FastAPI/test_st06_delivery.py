from datetime import datetime, timedelta

# literal을 쓰지 않고 상수를 쓰는 이유
# 2라는 숫자에 "배송일"이라고 표기하기 위해
# (미래의 동료, 미래의 나)에게 알려주는 역할
# magic number를 쓰지 말자
DELIVERY_DAYS = 2

# 매직 넘버(Magic number)는
# 코드에서 하드 코딩된(literal value) 일정한 값을 의미하는 숫자나 문자열 등을 의미합니다.
# 매직넘버는 코드 내에서 여러 곳에서 사용되지만 이 값의 의미나 목적은 코드에서 명확하게 알려지지 않습니다.
# 매직 넘버는 가독성이 떨어지고 유지보수가 어렵게 만들며, 예상치 못한 버그를 발생시키는 원인이 될 수 있습니다.
# 따라서 매직 넘버 대신에 상수나 변수를 사용하는 것이 좋습니다.
# 변수나 상수를 사용하면 값을 변경할 때 일괄적으로 변경할 수 있으므로 코드의 유지보수성과 가독성이 향상됩니다.

# 제품 코드
def _is_holiday(day: datetime) -> bool:
    "Return day of the week, where Monday == 0 ... Sunday == 6."
    return day.weekday() == 6  # 일요일이면 True

def get_eta(purchase_date: datetime) -> datetime:
    current_date = purchase_date
    remaining_days = DELIVERY_DAYS

    while remaining_days > 0:
        current_date += timedelta(days=1)
        if not _is_holiday(current_date):
            remaining_days -= 1

    return current_date

# 테스트 코드
def test_get_eta_2023_12_01() -> None:
    # Given : 재료를 준비합니다.
    order_date = datetime(2023,12,1)

    # When : 테스트 대상이 되는 함수를 호출합니다.
    result = get_eta(order_date)

    # Then : 결과
    assert result == datetime(2023,12,4)

def test_get_eta_2024_12_31() -> None:
    """
    실전에서는 공휴일 API를 호출해서 공휴일까지 계산
    공휴일 정보가 없어서 1월 1일도 평일로 취급
    """

    result = get_eta(datetime(2024,12,31))
    assert result == datetime(2025, 1, 2)

def test_get_eta_2024_02_28() -> None:
    result = get_eta(datetime(2024, 2, 28))
    assert result == datetime(2024, 3, 1)

def test_get_eta_2023_02_28() -> None:
    result = get_eta(datetime(2023, 2, 28))
    assert result == datetime(2023, 3, 2)

# Xunit 계열 테스트와 단위테스트의 역사
# 우리가 배운 단위 테스트를 Xunit 계열 테스트 라고도 부릅니다.
# 단위테스트의 시초는 켄트백(Kent Beck)이 처음 Small Talk 에서 작성한 SUnit 으로 알려져 있습니다.
# 이후 켄트백 본인이 Eric Gamma 라는 개발자와 함께 Java 에도 단위테스트 프레임워크인 Junit 을 만들었고 Junit 은 대성공했습니다.
# 그 이후 비슷한 프레임워크들이 ?Unit 이라는 이름으로 수많은 다른 언어에 (파이썬에는 내장 라이브러리인 unit test 와 pytest 가 있습니다) 퍼져나가게 됩니다.