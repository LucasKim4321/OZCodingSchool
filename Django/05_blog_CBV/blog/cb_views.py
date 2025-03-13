from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Blog


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

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    # pk_url_kwarg = 'blog_id'  # url에서 pk말고 다른 이름으로 id값 가져올 시 설정

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
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['test'] = 'CBV'
    #     return context

# LoginRequiredMixin  @login_required 와 동일한 기능
class BlogCreateView(LoginRequiredMixin,CreateView):
    model = Blog
    template_name = 'blog_create.html'
    # form 설정
    # fields = '__all__'
    fields = ('category','title','content')
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
    def get_success_url(self):
        return reverse_lazy('blog:detail', kwargs={'pk':self.object.pk})

class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    template_name = 'blog_update.html'
    fields = ('category','title','content')

    # 로그인 유저와 작성자가 같을 때만 수정 가능하게 처리
    # 1
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)
    # 2
    # def get_object(self, queryset=None):
    #     self.object = super().get_object(queryset)
    #     if self.object.author != self.request.user:
    #         raise Http404
    #     return self.object

    # update 성공 시 동작
    # def get_success_url(self):
        # return reverse_lazy('cb_blog_detail', kwargs={'pk':self.object.pk})
    # get_success_url이 없으면 model의 get_absolute_url찾아서 처리

class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog

    # 로그인 유저와 작성자가 같을 때만 삭제 가능하게 처리
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)

    # delete 성공 시 동작
    def get_success_url(self):
        return reverse_lazy('blog:list')
