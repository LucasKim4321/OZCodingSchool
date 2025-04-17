# User API
from typing import List

from fastapi import APIRouter, HTTPException
from starlette import status

from user.request import UserSignUpRequest
from user.response import UserResponse

router = APIRouter(prefix="/api/v1/users", tags=["User"])

USERS = [
    {"id":1, "username": "alice", "age":20},
    {"id":1, "username": "bob", "age":30},
    {"id":1, "username": "chalie", "age":40},
]

# 전체 유저 목록 조회
@router.get(
    "",
    description="##전체 유저 목록 조회 API",
)
# def get_users():
# def get_users() -> List[dict[str, str | int]]:  # [{"str":"str or int"}]
def get_users() -> List[UserResponse]:  # [{"str":"str or int"}]
    return USERS



# 새로운 유저 추가(=회원가입)
@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
)
def create_user(
    body: UserSignUpRequest,  # Type Hint로 적어주면 Request body로 요청을 받음.
):
    # 조건을 만족하지 않으면 에러 메시지 보냄
    # if body.age < 20:
    #     raise HTTPException(
    #         status_code=status.HTTP_400_BAD_REQUEST,
    #         detail= "age should be greater than 20",
    #     )
    new_user = {
        "id":len(USERS) + 1,
        "username": body.username,
        "age":body.age
    }
    USERS.append(new_user)
    return new_user