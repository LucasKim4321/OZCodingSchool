from django.contrib import admin
from blog.models import Blog, Comment

admin.site.register(Comment)

# TabularInline 표로 만들어서 inline으로 넣어주는 기능
class CommentInline(admin.TabularInline):
    model = Comment
    fields = ['content', 'author']
    extra = 1  # 기본 3개

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]