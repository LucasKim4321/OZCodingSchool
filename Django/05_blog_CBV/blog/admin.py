from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from blog.models import Blog, Comment

admin.site.register(Comment)

# TabularInline 표로 만들어서 inline으로 넣어주는 기능
class CommentInline(admin.TabularInline):
    model = Comment
    fields = ['content', 'author']
    extra = 1  # 기본 3개

@admin.register(Blog)
# class BlogAdmin(admin.ModelAdmin):
class BlogAdmin(SummernoteModelAdmin):
    summernote_fields = ['content',]
    inlines = [
        CommentInline,
    ]
