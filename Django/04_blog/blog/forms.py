from django import forms
from blog.models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        # fields = '__all__'  # 전체 적용
        fields = ('title','content')  # 원하는 것만 적용
