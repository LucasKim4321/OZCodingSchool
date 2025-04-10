# 이 특정 라인에 대해서 lint를 하고싶지 않을 때 주석 noqa사용
# noqa 사용되지 않는 import일지라도 import 하고 싶을 때 사용
# import st02 # noqa  # isort 옵션 사용할 때 이것 때문에 무시 될 수 있음.

# 일부러 알파벳순
import os
import sys

# 코드가 옆으로 길면 black 실행 시 이렇게 바꿔줌
# print(
#     "Lif is Tooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo Short!!"
# )

# ruff가 권한하지 않는 변수명
# O = "abc"


# black .
# poetry run black .



# 기본 그룹(select = ["E4", "E7", "E9", "F"]) 검사
# ruff check
# ruff check --fix

# 오직 I 그룹(import 관련) 문제만 검사
# ruff check --select I
# ruff check --select I --fix


# poetry
# pyproject.toml 설정
#
# [tool.black]
# line-length = 120  # hard wrap length 120
#
# [tool.ruff]
# target-version = "py313"  # 파이썬 버전 3.13

# ## 반드시 지켜야 하는 습관
#  - commit 하기 전에 자기가 무엇을 커밋하는지 꼭 확인하기!
#  - 미쳐 삭제하지 않은 print()가 없는지 꼭 확인하기
#   - print()는 "비싼 연산" 입니다.

# print()는 터미널에 입출력(Input Output)해야하기 때문에 오래걸림.
