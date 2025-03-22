from io import BytesIO
from pathlib import Path

from PIL import Image
from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from django.db import models
from django.urls import reverse
from utils.models import TimestampModel

# from django.contrib.auth.models import User
User = get_user_model()  # 장고에 설정되어있는 유저를 가져오는 함수

# Blog 구조
# 제목
# 본문
# 작성자
# 작성일자
# 수정일자
# 카테고리
# 썸네일이미지 - 미구현
# 태그 - 미구현

class Blog(TimestampModel):
    CATEGORY_CHOICES = (
        ('free','자유'),
        ('travel','여행'),
        ('cat','고양이'),
        ('dog','개'),
    )
    # blog.objects.filter(category__isnull=true) # Null인 데이터 확인
    # Blog.objects.filter(category='')  # 비어있는 데이터 확인
    # Blog.objects.filter(category='').update(category='free')
    category = models.CharField('카테고리', max_length=20, choices=CATEGORY_CHOICES, default='free')
    title = models.CharField('제목', max_length=100)
    content = models.TextField('본문')
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # author_id

    image = models.ImageField('이미지', null=True, blank=True, upload_to='blog/%Y/%m/%d')
    thumbnail = models.ImageField('썸네일', null=True, blank=True, upload_to="blog/%Y/%m/%d/thumbnail")
    # 2024/4/23일
    # blog/2024/4/23/이미지파일.jpg
    # ImageField, FieldField와 같은데 이미지만 업로드하게 되어있다.
    # varchar => 경로만 저장을 함
    # 이미지 필드를 사용하기 위해 pillow설  poetry add pillow

    # models.CASCATE => 같이 삭제 => 유저 삭제시 같이 블로그도 같이 삭제
    # models.PROTECT => 삭제가 불가능함 => 유저를 삭제하려고 할 때 블로그가 있으면 유저 삭제가 불가능 (기본값)
    # models.SET_NULL => 널 값을 넣음 => 유저 삭제시 블로그의 author가 Null이 됨.

    # 기존에 없던 author를 외례키로 추가하면 기존 블로그의 author값이 없어서 마이그레이션 할 때 에러남
    # python3 manage.py makemigrations 하면 기존 블로그 데이터에 기본값을 줄건지 물어봄.
    # 1번 기본값 주기 선택 후 기존 데이터의 초기값으로 주어질 id값 선택 하면 정상적으로 마이그레이션 됨.

    # TimestampModel에서 created_at, updated_at을 상속받음
    # created_at = models.DateTimeField('작성일자', auto_now_add=True)
    # updated_at = models.DateTimeField('수정일자', auto_now_add=True)

    def __str__(self):
        return f'[{self.get_category_display()}] {self.title[:10]}'

    # get_absolute_url은 보통 detail페이지
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'blog_pk':self.pk})

    # 썸네일 이미지 가져오는 함수
    def get_thumbnail_image_url(self):
        if self.thumbnail:
            return self.thumbnail.url
        elif self.image:
            return self.image.url
        return None

    # save()함수 override
    def save(self, *args, **kwargs): # *args 리스트 **kwargs 키워드
        if not self.image:
            return super().save(*args, **kwargs)

        image = Image.open(self.image)
        image.thumbnail((300, 300))
        image_path = Path(self.image.name)
        thumbnail_name = image_path.stem # /blog/2024/4/23/database.png => 파일 이름만 불러옴
        thumbnail_extension = image_path.suffix.lower() # 파일의 확장자를 가져옴 # 소문자로 바꿔서 처리
        thumbnail_filename = f'{thumbnail_name}_thumb{thumbnail_extension}' # 이름_thumb.확장자

        if thumbnail_extension in ['.jpg','jpeg']:
            file_type = 'JPEG'  # jpg일때 처리가 안되서 바꿔서 처리
        elif thumbnail_extension == '.gif':
            file_type = 'GIF'
        elif thumbnail_extension == '.png':
            file_type = 'PNG'
        else:
            return super().save(*args, **kwargs)

        temp_thumb = BytesIO()
        image.save(temp_thumb, file_type)
        temp_thumb.seek(0)
        thumb_file = ContentFile(temp_thumb.read())  # File 타입이 아니라서 생기는 오류 해결
        self.thumbnail.save(thumbnail_filename, thumb_file, save=False)
        temp_thumb.close()
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = '블로그'
        verbose_name_plural = '블로그 목록'

# Comment 구조
# blog정보
# 댓글 내용
# 작성자
# 작성일자
# 수정일자
# 카테고리

class Comment(TimestampModel):
    # TimestampModel에서 created_at, updated_at을 상속받음
    # created_at = models.DateTimeField('작성일자', auto_now_add=True)
    # updated_at = models.DateTimeField('수정일자', auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    content = models.CharField('본문', max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.blog.title} 댓글'

    class Meta:
        verbose_name = '댓글'
        verbose_name_plural = '댓글 목록'
        ordering = ('-created_at', '-id',) # 댓글 최신순으로 정렬
