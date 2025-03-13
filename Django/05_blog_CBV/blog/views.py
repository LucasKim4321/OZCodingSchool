from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import Http404
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from blog.forms import BlogForm
from blog.models import Blog

def blog_list(request):
    # order_by('정렬 기준 값') 오름차순(ASC)으로 정렬.  값에 '-'를 붙이면 내림차순(DESC)정렬
    blogs = Blog.objects.all().order_by('-created_at')
    # blogs = Blog.objects.all().order_by('-created_at')[10:21]

    q = request.GET.get('q')
    if q:
        blogs = blogs.filter(Q(title__icontains=q) | Q(content__icontains=q))
        # blogs = blogs.filter(title__icontains=q)

    paginator = Paginator(blogs, 10)  # blogs를 10개 단위로 페이지를 만듬
    page = request.GET.get('page')  # 파라미터 값으로 page값이 들어오면 page값 반환. 0이거나 최대페이지를 초과하는 페이지는 마지막 페이지를 반환. 숫자가 아닌값이 들어오면 첫페이지
    page_object = paginator.get_page(page)  # 해당 페이지로 이동

    # visit을 키값으로 쿠키를 가져오고 존재하지 않으면 0 있으면 +1
    visits = int(request.COOKIES.get('visits', 0 )) + 1

    request.session['count'] = request.session.get('count', 0) +1

    context = {
        # 'blogs': blogs,
        'count': request.session['count'],
        'object_list': page_object.object_list,
        'page_obj': page_object,
    }

    response =  render(request, 'blog_list.html', context)

    response.set_cookie('visits', visits)

    return response

    # templates 경로에 있을 시
    # return render(request, 'blog_list.html', context)
    # templates/blog 경로에 파일이 있을 시
    # return render(request, 'blog/blog_list.html', context)

def blog_detail(request, pk):
    # blog = Blog.objects.get(pk=pk)
    blog = get_object_or_404(Blog, pk=pk)
    context = {
        'blog':blog,
    }
    return render(request, 'blog_detail.html', context)

@login_required # settings.py에 설정된 LOGIN_URL로 리다이렉트
def blog_create(request):

    # 로그인되어 있지 않으면 로그인화면으로 리다이렉트
    # if not request.user.is_authenticated:
    #     return redirect(reverse('login'))

    # if request.method == 'POST':
    #     form = BlogForm(request.POST)
    #     if form.is_valid():
    #         blog = form.save() # form.save() : form에 내용을 DB에 반영하고 해당 데이터의 객체를 반환(리턴)함.
    #         return redirect(reverse('blog_detail'), {'pk':blog.pk})
    # else:
    #     form = BlogForm()

    form = BlogForm(request.POST or None)
    if form.is_valid():
        # form.save() : form에 내용을 DB에 반영하고 해당 데이터의 객체를 반환(리턴)함.
        blog = form.save(commit=False)  # DB에 반영하지 않고 객체만 반환함.
        blog.author = request.user  # 작성자에 로그인된 유저를 넣음
        blog.save()  # DB에 반영
        return redirect(reverse('fb:detail', kwargs={'pk':blog.pk}))

    context = {
        'form':form,
    }

    return render(request, 'blog_create.html', context)

@login_required
def blog_update(request, pk):
    # blog = get_object_or_404(Blog, pk=pk)
    # if request.user != blog.author:
    #     raise Http404
    blog = get_object_or_404(Blog, pk=pk, author=request.user) # pk와 author가 일치하는 데이터만 가져옴

    form = BlogForm(request.POST or None, instance=blog)  # instance 폼의 항목에 맞게 blog에서 데이터를 불러옴
    if form.is_valid():
        # form.save() : form에 내용을 DB에 반영하고 해당 데이터의 객체를 반환(리턴)함.
        blog = form.save()  # DB에 반영
        return redirect(reverse('fb:detail', kwargs={'pk':blog.pk}))

    context = {
        'blog':blog,
        'form':form,
   }

    return render(request, 'blog_update.html', context)


@login_required
@require_http_methods(['POST'])
def blog_delete(request, pk):
    # if request.method != 'POST':
    #     raise Http404

    blog = get_object_or_404(Blog, pk=pk, author=request.user) # pk와 author가 일치하는 데이터만 가져옴
    blog.delete()

    return redirect(reverse('fb:list'))

