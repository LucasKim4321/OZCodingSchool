from pydantic import BaseModel, field_validator


# User 앱에서 사용하는 Request Body 클래스

# 역직렬화 :  JSON -> Python
# 사용자로부터 넘겨받을 데이터를 클래스로 표현
# class UserSignUpRequest(BaseModel):
#     username: str
#     age: int
#
#     # 조건을 만족하지 않으면 에러 메시지 보냄
#     @field_validator("age")
#     @classmethod
#     def validate_age(cls, age: int):
#         if age < 20:
#             raise ValueError("age must be at least 20")
#         return age


# DRF Serializer
# 1) Serialize(직렬화)     :  Python -> JSON
# 2) Deserialize(역직렬화)  : JSON -> Python  => 클라이언트 요청 본문 -> body

class UserSignUpRequest(BaseModel):
    username: str
    password: str
