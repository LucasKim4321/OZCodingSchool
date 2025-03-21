"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect, render
from django.urls import path, include, reverse
from django.views.generic import TemplateView, RedirectView
from django.views import View
from blog import views as blog_views
from member import views as member_views
from blog import cb_views

def index(reqeust):
    # return redirect('blog/')
    return redirect(reverse('blog:list'))

class AboutView(TemplateView):
    template_name='about.html'

class TestView(View):
    def get(self, request):
        return render(request, 'test_get.html')
    def post(self, request):
        return render(request, 'test_post.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    # include 기능 사용
    # FBV blog
    path('fb/', include('blog.fbv_urls')),  # 경로에 fb/추가됨. # fb/
    # CBV blog
    path('blog/', include('blog.urls')),  # blog/
    # login 기능
    path('accounts/', include('django.contrib.auth.urls')), # include() 장고에 내장된 url사용
    path('signup/', member_views.sign_up, name = 'signup'),
    path('login/', member_views.login, name = 'login'),
    # test
    # path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('about/', AboutView.as_view(), name='about'),
    path('redirect/', RedirectView.as_view(pattern_name='about'), name='redirect'),
    path('redirect2/', lambda req: redirect('about')),
    path('test/', TestView.as_view(), name='test'),
    #summernote
    path('summernote/', include('django_summernote.urls')),
]

# config.settings 보단 django.conf의 settings가 나음.
# 현재 장고 실행환경에서 셋팅을 불러옴.  배포환경에서는 경로가 달라질 수 있기 때문에 이렇게함.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # django.conf.urls.static
