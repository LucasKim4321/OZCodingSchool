from django.urls import path
from blog import cb_views
from blog import views

app_name = 'blog'

urlpatterns = [
    # CBV blog
    path('', cb_views.BlogListView.as_view(), name = 'list'),
    path('<int:blog_pk>/', cb_views.BlogDetailView.as_view(), name = 'detail'),
    path('create/', cb_views.BlogCreateView.as_view(), name = 'create'),
    path('<int:pk>/update/', cb_views.BlogUpdateView.as_view(), name = 'update'),
    # path('<int:pk>/update/', views.blog_update, name = 'update'), # FBV로 테스트
    path('<int:pk>/delete/', cb_views.BlogDeleteView.as_view(), name = 'delete'),
    path('comment/create/<int:blog_pk>/', cb_views.CommentCreateView.as_view(), name = 'comment-create'),
]

# # url불러올 때 app_name:name
# # html에서 불러오기
# {% url 'blog:detail' blog.pk %}
# {% url 'blog:list' %}
#
# # python에서 불러오기
# reverse_lazy('blog:list')
# redirect(reverse('blog:list'))

# request.user.is_staff
# request.user.is_superuser