def add(a: int, b: int) -> int:
    return a + b


def mul(a: int, b: int) -> int:
    return a * b


# (테스트 도중 한 번이라도 실행된 제품 코드) / (전체 제품 코드)

# coverage 설치
# poetry add --group=dev coverage

# pytest를 사용해 coverage를 실행
# poetry run coverage run -m pytest st07_temp.py

# 보고서 작성
# -m, --show-missing
# Show line numbers of statements in each module that weren't executed.
# poetry run coverage report -m


# 결과 : 총 8줄 중에 5번 줄 한줄이 실행 되지 않았음을 의미
# test 코드도 포함되서 계산됨.
# Name           Stmts   Miss  Cover   Missing
# --------------------------------------------
# st07_temp.py       8      1    88%   5
# --------------------------------------------
# TOTAL              8      1    88%

# test 코드는 포함 되지 않게 설정
# */test_*.py 어느 경로든 'test_.py'라는 이름이 포함되면 제외
# [tool.coverage.run]
# omit = ["*/*test_*.py"]

# 테스트 코드를 블록 설정한 다음에 -> 우클릭 refactor -> move 하면
# 코드만 따로 때서 파일을 하나 만듬.

# 때어낸 파이썬 코드를 테스트
# poetry run coverage run -m pytest st07_test_temp.py

# 확인해보면 테스트 코드가 제외되고 실행됨
# poetry run coverage report -m

# 3/4 75%
# 커버리지가 75%로 감소했지만 이게 정상.
# 커버리지는 높을 수록 좋음.
# Name           Stmts   Miss  Cover   Missing
# --------------------------------------------
# st07_temp.py       4      1    75%   5
# --------------------------------------------
# TOTAL              4      1    75%

# poetry run coverage html
# htmlcov 폴더가 생김
# index.html을 열어보면 결과가 웹페이지에 보기좋게 표시됨.
# (테스트 도중 한 번이라도 실행된 제품 코드) / (전체 제품 코드)
# 2 / 4

# coverage 설치
# poetry add --group=dev coverage

# pytest를 사용해 coverage를 실행
# poetry run coverage run -m pytest st07_temp.py

# 보고서 작성
# -m, --show-missing
# Show line numbers of statements in each module that weren't executed.
# poetry run coverage report -m


# 결과 : 총 8줄 중에 5번 줄 한줄이 실행 되지 않았음을 의미
# test 코드도 포함되서 계산됨.
# Name           Stmts   Miss  Cover   Missing
# --------------------------------------------
# st07_temp.py       8      1    88%   5
# --------------------------------------------
# TOTAL              8      1    88%

# test 코드는 포함 되지 않게 설정
# */test_*.py 어느 경로든 'test_.py'라는 이름이 포함되면 제외
# [tool.coverage.run]
# omit = ["*/*test_*.py"]

# 테스트 코드를 블록 설정한 다음에 -> 우클릭 refactor -> move 하면
# 코드만 따로 때서 파일을 하나 만듬.

# 때어낸 파이썬 코드를 테스트
# poetry run coverage run -m pytest st07_test_temp.py

# 확인해보면 테스트 코드가 제외되고 실행됨
# poetry run coverage report -m

# 3/4 75%
# 커버리지가 75%로 감소했지만 이게 정상.
# 커버리지는 높을 수록 좋음.
# Name           Stmts   Miss  Cover   Missing
# --------------------------------------------
# st07_temp.py       4      1    75%   5
# --------------------------------------------
# TOTAL              4      1    75%

# poetry run coverage html
# htmlcov 폴더가 생김
# index.html을 열어보면 결과가 웹페이지에 보기좋게 표시됨.

# ## 정리
#
#   - 단위 테스트를 전부 실행해도 한 번도 실행되지 않은 코드는 곧 테스트를 안한 코드다.
#   - 테스트 안 된 지점에서 버그가 나면 할 말이 없다. (테스트 안 한 개발자의 잘못)
#   - 따라서 커버리지 계산을 통해 “지금 내가 수정한 코드가 제대로 테스트 되고 있는가” 를 판단할 필요가 있다.
#   - 커버리지의 정의는 (테스트 도중 한번이라도 실행된 제품코드) ÷ (전체제품코드) 이다.
#   - 커버리지를 계산할 때 테스트 코드는 omit 하고, 제품 코드만 계산에 들어가도록 해야 한다.
#
#   - 커버리지 실행을 하려면
#     - poetry run coverage run -m pytest .
#     - poetry run coverage report -m
#     - poetry run coverage html
#   을 하면 됩니다.
