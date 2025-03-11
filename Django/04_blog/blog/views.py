from django.shortcuts import render, get_object_or_404
from blog.models import Blog

def blog_list(request):
    blogs = Blog.objects.all()

    # visit을 키값으로 쿠키를 가져오고 존재하지 않으면 0 있으면 +1
    visits = int(request.COOKIES.get('visits', 0 )) + 1

    request.session['count'] = request.session.get('count', 0) +1

    context = {
        'blogs': blogs,
        'count': request.session['count'],
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
    context = {'blog':blog}
    return render(request, 'blog_detail.html', context)