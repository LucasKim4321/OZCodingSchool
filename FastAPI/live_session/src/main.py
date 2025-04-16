from fastapi import FastAPI, Query, HTTPException, Path
from pydantic import BaseModel

app = FastAPI()

# Pydantic으로 클라이언트로부터 넘겨받을 데이터를 표현
class UserSignUpRequest(BaseModel):
    username: str
    password: str

# Request Body
@app.post("/users")
# root_handler함수에서 처리한다.
def user_handler3(
        body: UserSignUpRequest,  # Type Hint로 적어줌.
):
    return  {
        "username": body.username,
        "password": "<PASSWORD>" + body.password,
    }

# Routing, Path, Query Parameter, Request Body


# API Path(경로)
# 1) Path 변수 : 동적으로 URL 경로를 통해 값을 넘길 때
# 2) Query Parameter: URL 경로를 통해 쿼리 조건을 넘길 때 (필수 x)
@app.get("/users/{username}")
# root_handler함수에서 처리한다.
def user_handler(
        username: str = Path(min_length=2, max_length=8),
        age: int = Query(default=None, ge=20, lt=100)
):
    # return {"message": "Hello World"}
    # return [{"id":1, "username": "elon"}]

    return  {
        "username": username,
        "age": age
    }

# 파라미터 값이 필요한데 안들어오면 422에러 발생
# 필수가 아니게 설정하려면 default값을 줘서 설정
@app.get("/users")
# root_handler함수에서 처리한다.
# def root_handler(age: int = None):  # None -> null
# def root_handler(age: int  = Query(..., ge=20, lt=100)):
# def root_handler(age: int  = Query(default=None, ge=20, lt=100)):
def user_handler2(age: int  = Query(default=None, ge=20, lt=100)):  # default 값 설정
    # if 20 <= age < 100:
    return {"age": age}


# Pydantic(FastAPI) == DRF Serializer(Django)

# 404 -> 경로 자체가 없음. 패턴 매칭 실패.
# 422 -> 경로는 맞는데, 경로의 조건이 안맞음.

# 1. Query Parameter 쓰는 방법
# GET /users?age=30&name=elon&lang=kor
# 하나의 url에서 여러개의 파라미터를 받을 수 있다.

# 2. 경로를 통해서 표현하는 방법
# GET /users/age/30
# 여러개의 path변수를 받으려면 문제가 많다.

# Resource(자원)
# : 사용자(나이, 이름, 등)


# 서버 실행을 위해 경로 이동
# cd src

# 개발 모드로 실행
# fastapi dev
# 다른 모드도 있음.

# Swagger API문서
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc
