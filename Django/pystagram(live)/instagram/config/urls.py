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
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from config.settings import base as base_settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("users/", include("user.urls")),  # 유저 앱 라우팅
    path("", include("feed.urls")),  # 피드 앱 라우팅
# ]
] + static(base_settings.STATIC_URL, document_root=base_settings.STATIC_ROOT) # 로컬 환경에서 설정
# static경로에 접근가능하게 설정
