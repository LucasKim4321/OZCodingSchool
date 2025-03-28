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

# AbstractUser: username(unique), email(중복)
# CustomUser: email(unique)

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'  # USERNAME 사용자를 고유하게 식별하는 기준 설정
    REQUIRED_FIELDS = ['username']
    # EMAIL_FIELD = 'email'
