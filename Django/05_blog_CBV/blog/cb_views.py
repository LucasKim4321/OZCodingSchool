from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.forms import CommentForm, BlogForm
from blog.models import Blog, Comment


class BlogListView(ListView):
    # model = Blog # object.all()을 사용해 데이터를 가져옴.
    # ordering = ('-created_at',)  # 정렬 옵션
    queryset = Blog.objects.all().order_by('-created_at')  # 사용자 지정 query
    template_name = 'blog_list.html'  # render()할 페이지
    paginate_by = 10  # paginator 설정

    # 사용자 지정 쿼리셋
    def get_queryset(self):
        queryset = super().get_queryset()  # 쿼리 셋을 가져옴
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(
                Q(title__icontains=q) |
                Q(content__icontains = q)
            )
        return queryset

# context = {
#     "paginator": paginator,
#     "page_obj": page,
#     "is_paginated": is_paginated,
#     "object_list": queryset,
# }

# 기존 디테일뷰
# class BlogDetailView(DetailView):
#     model = Blog
#     글을 불러올때 댓글도 같이 불러오게 설정. 설정하지 않으면 요청을 두 번하게됨.
#     queryset = Blog.objects.all().prefetch_related('comment_set', 'comment_set__author')
#     Django에서는 ForeignKey(외래 키) 관계가 설정되면, 역참조(Reverse Lookup)를 위한 관련 매니저가 자동으로 생성됩니다.
#     즉, Comment 모델이 Blog 모델을 참조하고 있다면, Django는 자동으로 blog.comment_set이라는 매니저를 제공하여 해당 Blog 객체에 연결된 모든 Comment를 가져올 수 있도록 합니다.
# 상세 페이지에서 댓글 페이지 기능을 사용하기 위해 리스트뷰를 사용
class BlogDetailView(ListView):  # 댓글
    model = Comment
    template_name = 'blog_detail.html'
    paginate_by = 10
    # pk_url_kwarg = 'blog_id'  # url에서 pk말고 다른 이름으로 id값 가져올 시 설정

    # 블로그 정보 불러옴.
    def get(self, request, *args, **kwargs):
        self.object = get_object_or_404(Blog, pk=kwargs.get('blog_pk'))
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return self.model.objects.filter(blog=self.object).prefetch_related('author')

    # 데이터 처리하는 방법 1
    # 사용자 지정 쿼리셋
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset.filter(id__lte=50)

    # 데이터 처리하는 방법 2
    # def get_object(self, queryset=None):
    #     # object = self.model.objects.get(pk=self.kwargs.get('pk'))
    #     object = super().get_object()
    #     if object.id > 50:
    #         raise Http404("해당 객체에 대한 접근이 금지되어있습니다.")
    #     return object

    # 사용자 지정 context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['blog'] = self.object
        return context

    # # post요청시
    # def post(self, *args, **kwargs):
    #     comment_form = CommentForm(self.request.POST)
    #
    #     if not comment_form.is_valid():
    #         self.object = self.get_object()
    #         context = self.get_context_data(object=self.object)
    #         context['comment_form'] = comment_form
    #         return self.render_to_response(context)
    #
    #     if not self.request.user.is_authenticated:
    #         raise Http404
    #
    #     comment = comment_form.save(commit=False)
    #     # comment.blog = self.get_object() # 블로그 정보 저장
    #     comment.blog_id = self.kwargs['pk']  # blog_id 직접 설정
    #     comment.author = self.request.user
    #     comment.save()
    #
    #     return HttpResponseRedirect( reverse_lazy('blog:detail', kwargs={'pk':self.kwargs['pk']}))

# LoginRequiredMixin  @login_required 와 동일한 기능
class BlogCreateView(LoginRequiredMixin,CreateView):
    model = Blog
    template_name = 'blog_form.html'
    # form 설정
    # fields = '__all__'
    # fields = ('category','title','content')
    form_class = BlogForm  # 써머노트 쓸 때 fields 대신 사용
    # success_url = reverse('cb_blog_list') # 서로가 서로를 임포트하는 서큘러 임포트가 발생
    # success_url = reverse_lazy('cb_blog_list')  # create 성공시 동작
    # success_url = reverse_lazy('cb_blog_detail', kwargs={'pk':object.pk})  # 오류남.

    # 작성자 생성 후 save()동작
    def form_valid(self, form):
        # blog = form.save(commit=False)
        # blog.object = form.save(commit=False)
        # blog.object.author = self.request.user
        # blog.object.save()
        # self.object = blog
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    # create 성공 시 동작
    # def get_success_url(self):
        # return reverse_lazy('cb_blog_detail', kwargs={'pk':self.object.pk})
    # get_success_url이 없으면 model의 get_absolute_url찾아서 처리

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sub_title'] = '작성'
        context['btn_name'] = '생성'
        return context

    #     test_dict = {
    #         'a' : 1,
    #         'b' : 2,
    #         'c' : 3,
    #     }
    #     self.test(a=test_dict['a'], b=test_dict['b'], c=test_dict['c'])
    #     self.test(**test_dict)
    #     test_list = [1,2,3]
    #     self.test(test_list[0], test_list[1], test_list[2])
    #     self.test(*test_list)
    #     return context
    # def test(self, a, b, c):
    #     return

class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    template_name = 'blog_form.html'
    # fields = ('category','title','content')
    form_class = BlogForm  # 써머노트 쓸 때 fields 대신 사용

    # 로그인 유저와 작성자가 같을 때만 수정 가능하게 처리
    # 1
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_superuser:
            return queryset
        return queryset.filter(author=self.request.user)
    # 2
    # def get_object(self, queryset=None):
    #     self.object = super().get_object(queryset)
    #     if self.object.author != self.request.user:
    #         raise Http404
    #     return self.object

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sub_title'] = '수정'
        context['btn_name'] = '수정'
        return context

    # update 성공 시 동작
    # def get_success_url(self):
        # return reverse_lazy('cb_blog_detail', kwargs={'pk':self.object.pk})
    # get_success_url이 없으면 model의 get_absolute_url찾아서 처리

class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog

    # 로그인 유저와 작성자가 같을 때만 삭제 가능하게 처리
    def get_queryset(self):
        queryset = super().get_queryset()
        # superuser가 아니면 로그인 유저와 글쓴이가 동일한 데이터만 반환
        # 조건문이 많아지면 not으로 쓰는걸 더 추천한다고 함.
        if not self.request.user.is_superuser:
            return queryset.filter(author=self.request.user)
        return queryset

    # delete 성공 시 동작
    def get_success_url(self):
        return reverse_lazy('blog:list')

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm

    def get(self, *args, **kwargs):
        raise Http404

    def form_valid(self, form):
        blog = self.get_blog()
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.blog = blog
        self.object.save()
        return HttpResponseRedirect(reverse('blog:detail', kwargs={'blog_pk':blog.pk} ))

    def get_blog(self):
        pk = self.kwargs['blog_pk']
        blog = get_object_or_404(Blog, pk=pk)
        return blog

# /comment/create/<int:blog_pk>/
