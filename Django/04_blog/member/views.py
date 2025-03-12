from django.conf import settings # 현재 실행중인 장고에서 settings를 가져오기 때문에 오류가 날 수 없음.
# from config import settings # 이렇게 하면 파일이름이 바뀌면 오류날 수 있음
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login, logout as django_logout
from django.urls import reverse

def sign_up(request):
    # username = request.POST['username'] # POST말고 다른 요청이 들어오면 브라우저에서 오류남.
    # username = request.POST.get('username') # 다른 요청이 들어오면 None이 발생하지만 오류가 나진 않음
    # print('username', username)

    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST) # POST요청 데이터를 여러 처리과정(validation등)을 거친 후 form에 넣음
    #     if form.is_valid(): # 요구 조건 통과 여부 확인
    #         form.save() # 요구 조건이 맞으면 저장
    #         return redirect('/accounts/login/')
    # else:
    #     form = UserCreationForm() # 장고에서 기본적으로 제공해주는 회원가입 폼

    # 이렇게 하면 조건문 안써도 됨.
    form = UserCreationForm(request.POST or None)
    if form.is_valid(): # 요구 조건 통과 여부 확인
        form.save() # 요구 조건이 맞으면 저장
        return redirect(settings.LOGIN_URL)

    context = {
        'form':form,
    }
    return render(request, 'registration/signup.html', context)

# 사용자 지정 로그인
def login(request):
    form = AuthenticationForm(request, request.POST or None)

    if form.is_valid(): # 요구 조건 통과 여부 확인
        django_login(request, form.get_user())  # 로그인을 시도함
        # next = request.GET['next']  # next가 없으면 오류남
        next = request.GET.get('next')  # next가 있으면 불러오고 없으면 None
        if next:
            return redirect(next)
        return redirect(reverse('blog_list'))  # html의 {% url 'blog_list' %} 와 동일

    context = {
        'form':form
    }
    return render(request, 'registration/login.html', context)