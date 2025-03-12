from django.contrib.auth import get_user_model
from django.db import models

# from django.contrib.auth.models import User
User = get_user_model()  # 장고에 설정되어있는 유저를 가져오는 함수

class Blog(models.Model):
    CATEGORY_CHOICES = (
        ('free','자유'),
        ('travel','여행'),
        ('cat','고양이'),
        ('dog','개'),
    )
    category = models.CharField('카테고리', max_length=20, choices=CATEGORY_CHOICES)
    title = models.CharField('제목', max_length=100)
    content = models.TextField('본문')
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # author_id
    # models.CASCATE => 같이 삭제 => 유저 삭제시 같이 블로그도 같이 삭제
    # models.PROTECT => 삭제가 불가능함 => 유저를 삭제하려고 할 때 블로그가 있으면 유저 삭제가 불가능 (기본값)
    # models.SET_NULL => 널 값을 넣음 => 유저 삭제시 블로그의 author가 Null이 됨.

    # 기존에 없던 author를 외례키로 추가하면 기존 블로그의 author값이 없어서 마이그레이션 할 때 에러남
    # python3 manage.py makemigrations 하면 기존 블로그 데이터에 기본값을 줄건지 물어봄.
    # 1번 기본값 주기 선택 후 기존 데이터의 초기값으로 주어질 id값 선택 하면 정상적으로 마이그레이션 됨.

    created_at = models.DateTimeField('작성일자', auto_now_add=True)
    updated_at = models.DateTimeField('수정일자', auto_now_add=True)

    def __str__(self):
        return f'[{self.get_category_display()}] {self.title[:10]}'

    class Meta:
        verbose_name = '블로그'
        verbose_name_plural = '블로그 목록'

# 제목
# 본문
# 작성자 => 패스 (추후 업데이트)
# 작성일자
# 수정일자
# 카테고리
# 썸네일이미지
# 태그