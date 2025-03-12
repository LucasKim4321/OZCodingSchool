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
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from blog import views as blog_views
from member import views as member_views

def index(reqeust):
    return redirect("/blog/")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('blog/', blog_views.blog_list, name = 'blog_list'),
    path('blog/<int:pk>/', blog_views.blog_detail, name = 'blog_detail'),
    path('create/', blog_views.blog_create, name = 'blog_create'),
    path('blog/<int:pk>/update/',blog_views.blog_update, name = 'blog_update'),
    path('<int:pk>/delete/', blog_views.blog_delete, name = 'blog_delete'),
    path('accounts/', include('django.contrib.auth.urls')), # include() 장고에 내장된 url사용
    path('signup/', member_views.sign_up, name = 'signup'),
    path('login/', member_views.login, name = 'login'),
]
