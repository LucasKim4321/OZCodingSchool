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
from django.http import HttpResponse, Http404
from django.shortcuts import render

movie_list = [
    {'title':'파묘','director':'장재현'},
    {'title':'웡카','director':'폴 킹'},
    {'title':'듄: 바트 2','director':'드니 빌뇌브'},
    {'title':'시민덕희','director':'박영주'},
]

book2_list = [
    {'title':'황편필의 진보를 위한 역사', 'author':'황현필', 'price':'19,800'},
    {'title':'모순', 'author':'양귀자', 'price':'11,700'},
    {'title':'초역 부처의 말', 'author':'코이케 류노스케', 'price':'16,020'},
    {'title':'해커스 토익 기출 VOCA(보카)', 'author':'David Cho', 'price':'11,610'},
]

def index(request):
    return HttpResponse('<h1>hello2</h1>')

def book_list(request):
    book_text = ''

    for i in range(0,10):
        book_text += f'book{i}<br>'
    return HttpResponse(book_text)

def book(request, num):
    book_text = f'book {num}번 페이지입니다.'
    return HttpResponse(book_text)

def language(request, lang):
    return HttpResponse(f'<h1>{lang}언어 페이지입니다.')

def python(request):
    return HttpResponse(f'<h1>python 페이지입니다.')

def movies(request):

    # 1
    # movie_titles = [movie['title'] for movie in movie_list]

    # 2
    # movie_title = []
    # for movie in movie_list:
    #     movie_titles.append(movie['title'])

    # 1
    # response_text = '<br>'.join(movie_titles)

    # 2
    # response_text = ''
    # for index, title in enumerate(movie_titles):
    #     response_text += f'<a href="/movie/{index}">{title}</a><br>'

    # 3
    movie_titles = [
        f'<a href="/movie/{index}">{movie["title"]}</a><br>'
        for index, movie in enumerate(movie_list)
    ]
    response_text = '<br>'.join(movie_titles)

    return HttpResponse(response_text)

def movie_detail(request, index):
    # 500번대 에러 서버측 에러
    # 400번대 에러 유저측 에러
    if index > len(movie_list)-1:
        raise Http404 # 잘못된 접근으로 인해 페이지가 없음

    movie = movie_list[index]
    response_text = f"<h1>{movie['title']}</h1> <p>감독: {movie['director']}</p>"
    return HttpResponse(response_text)

def movies2(request):

    return render(request, 'movies.html', {'movie_list':movie_list})
    # return render(request, template_name='movies.html', context={'movie_list':movie_list})

def movie2_detail(request, index):
    # 500번대 에러 서버측 에러
    # 400번대 에러 유저측 에러
    if index > len(movie_list)-1:
        raise Http404 # 잘못된 접근으로 인해 페이지가 없음

    context = {'movie':movie_list[index]}

    # context = {'movie_list':movie_list, 'index':index}

    return render(request, 'movie.html', context)

def books2(request):
    return render(request, 'books.html', {'books':book2_list, 'range':range(10)})

def book2(request, index):
    if index > len(book2_list)-1:
        raise Http404
    context = {'book':book2_list[index]}
    return render(request, 'book.html', context)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('book_list/', book_list),
    path('book_list/<int:num>/', book),
    path('language/<str:lang>/', language),  # <str>을 쓰면 모든 문자열이 인식되서 모든 경로에 영향을 끼침
    path('language/python/', python), # 마지막에 , 콤마 사용
    path('movie/', movies),
    path('movie/<int:index>/', movie_detail),
    path('movie2/', movies2),
    path('movie2/<int:index>/', movie2_detail),
    path('book2/', books2),
    path('book2/<int:index>/', book2)
]
