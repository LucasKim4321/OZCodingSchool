# Generator, Comprehension

**Generator**와 **Comprehension**은 Python에서 자주 사용되는 표현식인데, 서로 밀접하게 관련되어있다.

아래에 차이점과 예시를 함께 살펴보자.

---

## 🧠 1. Comprehension (컴프리헨션)

**리스트, 딕셔너리, 세트 등을 간결하게 생성**할 수 있는 문법입니다.

### ✅ 종류별 예시

### 🟦 List Comprehension

```python
python
복사편집
squares = [x ** 2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

```

### 🟩 Set Comprehension

```python
python
복사편집
unique = {x % 3 for x in range(10)}
print(unique)  # {0, 1, 2}

```

### 🟨 Dict Comprehension

```python
python
복사편집
square_dict = {x: x ** 2 for x in range(5)}
print(square_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

```

---

## ⚙️ 2. Generator Expression (제너레이터 표현식)

- List comprehension과 **비슷한 문법**이지만, **메모리를 절약**하면서 **하나씩 생성**하는 **이터레이터**를 반환합니다.
- **`()` 소괄호** 사용

```python
python
복사편집
gen = (x ** 2 for x in range(5))
print(gen)  # <generator object>
print(next(gen))  # 0
print(next(gen))  # 1

```

> ⚠️ list comprehension은 메모리에 전체 리스트를 저장하지만, generator expression은 필요할 때마다 값을 생성함 → 메모리 효율성 Good!
> 

---

## 🔍 주요 차이점 요약

| 항목 | Comprehension (List 등) | Generator Expression |
| --- | --- | --- |
| 괄호 | `[]`, `{}`, `{k: v}` | `()` |
| 결과 타입 | `list`, `set`, `dict` | `generator` |
| 메모리 사용 | 높음 (전체 저장) | 낮음 (lazy evaluation) |
| 사용 목적 | 모든 값을 한 번에 처리 | 큰 데이터, 반복 처리 |

---

필요하시면 실제 메모리 차이 비교 예제나, generator function (`yield` 사용)과의 차이점도 설명해드릴 수 있습니다!

# Imuutable, Mutable

"Immutable"과 "Mutable"은 프로그래밍에서 **데이터의 변경 가능성**을 설명할 때 사용하는 용어입니다.

---

### 🔒 Immutable (불변)

- **한번 생성되면 그 값을 변경할 수 없는 객체**
- 값을 바꾸려면 **새로운 객체**를 만들어야 함
- 예시 (Python):
    
    ```python
    python
    복사편집
    a = "hello"
    a[0] = "H"  # ❌ 오류 발생 (문자열은 immutable)
    
    ```
    
- 대표적인 immutable 객체:
    - `int`, `float`, `str`, `tuple`, `frozenset`

---

### 🔓 Mutable (가변)

- **생성 후에도 값을 변경할 수 있는 객체**
- 객체 자체를 수정할 수 있음 (원본이 바뀜)
- 예시 (Python):
    
    ```python
    python
    복사편집
    a = [1, 2, 3]
    a[0] = 100  # ✅ 리스트는 mutable
    print(a)  # [100, 2, 3]
    
    ```
    
- 대표적인 mutable 객체:
    - `list`, `dict`, `set`, 사용자 정의 클래스 객체 등

---

### 💡 요약

| 속성 | Immutable | Mutable |
| --- | --- | --- |
| 값 변경 | ❌ 불가능 | ✅ 가능 |
| 예시 | `int`, `str`, `tuple` | `list`, `dict`, `set` |
| 사용 시 주의 | 복사본 생성 필요 | 원본이 바뀔 수 있음 |