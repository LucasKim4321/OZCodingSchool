
print("12345")
a = 123

# reveal_type(a) # mypy로 검사 수행시 타입을 알려줌. mypy만 사용하는 함수. 파이썬으로 실행하면 오류걸림.

my_int: int = 123  # 타입 힌트로 int를 줬는데 str을 입력 받으면 mypy 검사시 오류남.


# 추론(inference)
my_int2 = 123  # Literal : 값  mypy는 리터럴로부터 타입을 추론함.


my_list: list[str] = ["a", "b", "c"]

# 불변성 (immutable)
# 튜플 타입에 타입 힌트를 주려면 길이만큼 타입을 지정
my_tuple: tuple[str,str,str] = ("a", "b", "c")

# 길이를 모르는 경우에 어떻게 할 까?
my_tuple2: tuple[str, ...] = ("a", "b", "c")

my_dict: dict[str, int] = {"a": 1, "b": 2, "c": 3}

# str이나 int타입 설정.
# bool도 통과된다. 파이썬의 bool이 int를 상속받았기 때문에 가능.
or_type_list: list[str|int] = ["a", 1, "c", 3, False]

def add(a: int, b: int) -> int:
    return a + b

1 + add(1,1)

