# User API
from typing import List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status

from database import SessionFactory, get_session
from user.models import User
from user.request import UserSignUpRequest
from user.response import UserResponse

router = APIRouter(prefix="/api/v1/users", tags=["User"])

USERS = [
    {"id":1, "username": "alice", "age":20},
    {"id":1, "username": "bob", "age":30},
    {"id":1, "username": "chalie", "age":40},
]

# 전체 유저 목록 조회
# @router.get(
#     "",
#     description="##전체 유저 목록 조회 API",
#     response_model=list[UserResponse],
# )
# def get_users():
# def get_users() -> List[dict[str, str | int]]:  # [{"str":"str or int"}]
# def get_users() -> List[UserResponse]:  # [{"str":"str or int"}]
#     return USERS

# @router.get(
#     "",
#     description="##전체 유저 목록 조회 API",
#     response_model=list[UserResponse],
# )
# def get_users() -> List[UserResponse]:  # [{"str":"str or int"}]
#     session = SessionFactory()
#     from select import select
#     result = session.execute(select(User))  # 테이블 데이터 조회
#     users = result.scalars()  # 데이터 -> User instance
#     return users

@router.get(
    "",
    description="##전체 유저 목록 조회 API",
    response_model=list[UserResponse],  # 타입 힌트처럼 FastAPI에 응답(Response)의 타입을 알려주는 역할. 이를 활용해 스웨거에 자동으로 생성된다.
)
# def get_users() -> List[dict[str, str | int]]:  # [{"str":"str or int"}]
def get_users(
        # session: Session = Depends(get_session),
) -> List[UserResponse]:  # [{"str":"str or int"}]

    session = SessionFactory()  # 데이터 베이스에 연걸 정보를
    result = session.query(User).all()
    users = result.scalars()  # 데이터 -> User instance
    return users



# 새로운 유저 추가(=회원가입)
# @router.post(
#     "",
#     status_code=status.HTTP_201_CREATED,
# )
# def create_user(
#     body: UserSignUpRequest,  # Type Hint로 적어주면 Request body로 요청을 받음.
# ):
#     # 조건을 만족하지 않으면 에러 메시지 보냄
#     # if body.age < 20:
#     #     raise HTTPException(
#     #         status_code=status.HTTP_400_BAD_REQUEST,
#     #         detail= "age should be greater than 20",
#     #     )
#
#     new_user = {
#         "id":len(USERS) + 1,
#         "username": body.username,
#         "age":body.age
#     }
#     USERS.append(new_user)

@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=UserResponse,
)
def create_user(
    body: UserSignUpRequest,  # Type Hint로 적어주면 Request body로 요청을 받음.
    session: Session = Depends(get_session),   # get_session 함수(일시중지 상태)
):
    # session = SessionFactory()

    new_user = User(username=body.username, password=body.password)
    session.add(new_user)
    session.commit()
    return new_user
