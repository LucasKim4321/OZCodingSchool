from django.db import models

# Model = DB의 테이블
# Field = DB의 컬럼

# 북마크
# 이름 => varchar
# URL주소 => varchar

# models.CharField == varchar
# models.URLField == varchar + url_validation
# models.DateTimeField == DateTime

class Bookmark(models.Model):
    name = models.CharField('이름', max_length=100)
    url = models.URLField('URL')
    created_at = models.DateTimeField('생성일시', auto_now_add=True) # 생성시 자동으로 현재 시간 추가
    updated_at = models.DateTimeField('수정일시', auto_now=True)

    # 관리자 페이지에서 bookmark object 라고 표시되는 사항 변경
    def __str__(self):
        return self.name
        # return f'{self.name} ({self.url})'

    class Meta: # 필수는 아니고 admin 등에서 사용 (없어도 무관)
        verbose_name = '북마크' # verbose_name 따로 지정. 지정하지 않으면 Bookmark
        verbose_name_plural = '북마크 목록'  # verbose_name_plural 따로 지정. 지정하지 않으면 Bookmarks

# 앱에 필요한 테이블 admin, auth, contenttypes, sessions
# 마이그레이션
# python3 manage.py migrate
# 마이그레이션 생성
# python3 manage.py makemigrations

# makemigrations => migration.py 파일을 생성
# 실제 DB에는 영향 x => 실제 DB에 넣기위한 정의를 하는 파일을 생성
# migrate => migrations/ 폴더 안에 있는 migration 파일들을 실제 DB에 적용.