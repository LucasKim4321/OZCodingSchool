from django.contrib import admin
from bookmark.models import Bookmark

@admin.register(Bookmark)  # admin.site.register(Bookmark, BookmarkAdmin)한거랑 똑같은 동작이 일어남
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['id','name','url','created_at','updated_at']  # 표시할 컬럼 설정
    list_display_links = ['name','url']  # 링크 기능 추가
    list_filter = ['name','url']  # 필터링 기능 추가

# admin.site.register(Bookmark, BookmarkAdmin)