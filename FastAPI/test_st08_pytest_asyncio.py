# st08_test_pytest_asyncio.py


# async 함수는 기본적으로 pytest 테스트에서 무시됨.
async def test_abc() -> None:
    print("abc")


def main() -> None:
    print("hihi")


# pytest-asyncio 설치
# poetry add --group=dev pytest-asyncio

# 오류없이 코딩 후
# 코드 포매터로 포메팅
# black .
#
# $? 가장 최근에 실행된 명령어의 종료 상태(exit code)를 출력하는 명령어입니다.
# echo $?
#
# 출력 0 문제 없음
# 0 이상이면 문제 있음
#
# 오류가 있는 코드를 짠 후
# black .
#
# echo $?
#
# 출력이 0보다 크면 문제있음.
