from datetime import datetime

from pydantic import BaseModel


# 응답을 반환하는 클래스

# 직렬화 : Python -> JSON
class UserResponse(BaseModel):
    id: int
    username: str
    password: str
    created_at: datetime
