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
from django.http import HttpResponse
from django.urls import path
from django.shortcuts import render, redirect

def index(request):
    response_text = ("<h1>index page</h1>"
                     "<a href=gugudan/>구구단</a>")
    return HttpResponse(response_text)
def gugudan_list(request):
    return render(request, 'gugudan_list.html', {'range':range(1,10)})

def gugudan(request, dan):
    # 300번대 리다이렉트 관련
    if dan < 2:
        return redirect('/gugudan/2/')
    context = {
        'dan':dan,
        'results': [dan * i for i in range(1, 10)],  # 1번째 방법
        # 'results': [(i, dan * i) for i in range(1, 10)],  # 2번째 방법
        # 'range':range(1,10)  # 3번째 방법
    }
    return render(request, 'gugudan.html', context)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('gugudan/', gugudan_list),
    path('gugudan/<int:dan>/', gugudan),
]
