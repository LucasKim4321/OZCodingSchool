# Django에서 회원관리 기능 구현하는 방법

# 1. Django에 내장된 User 모델 사용
# 장점: 간단함, 조금 더 안전, 검증된 코드
# 단점: 커스텀 어려움, 필요하지 않는 컬럼(데이터)까지도 저장
# from django.contrib.auth.models import User
# 내장된 기능 사용
# python manage.py createsuperuser -> User(is_staff=True, is_admin=True)

# 2. AbStractUser 상속 받아서 필요한 부분만 사용
# from django.contrib.auth.models import AbstractUser

# 3. 처음부터 직접 다 구현
# 장점: 내 마음대로, 직관적
# 단점: 귀찬다, 실수, 보안

# 장고 기본 유저 적용 안되도록 설정. 유저를 커스텀 할 거면 첫 마이그레이션 전에 미리 해야함.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.constraints import UniqueConstraint


# AbstractUser: username(unique), email(중복)
# CustomUser: email(unique)

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    # USERNAME_FIELD : 사용자의 인증에 사용할 필드를 지정하는 속성
    USERNAME_FIELD = 'email'  # USERNAME 사용자를 고유하게 식별하는 기준 설정
    # REQUIRED_FIELDS : 사용자 생성시 필수로 입력해야 하는 필드
    REQUIRED_FIELDS = ['username']  # email, username, password 필수

class Follow(models.Model):
    # related_name 기본값 : 컬럼이름_set
    # on_delete = models.CASCADE 유저 삭제시 follow도 삭제
    user = models.ForeignKey(CustomUser, related_name="followers", on_delete=models.CASCADE) # 팔로우 대상 사용자
    follower = models.ForeignKey(CustomUser, related_name="followings", on_delete=models.CASCADE) # 팔로우 하는 사용자
    created_at = models.DateTimeField(auto_now_add=True)  # 생성된 시점의 시간을 저장

    class Meta:
        # 제약 규칙 (constraints)
        # 동일한 관계 중복 방지
        constraints = [
            UniqueConstraint(fields=["user", "follower"], name="unique_follow_relationship")
        ]
        ordering = ['-created_at']  # 최신순 정렬

    def __str__(self):
        return f"{self.follower_id} -> {self.user_id}"
