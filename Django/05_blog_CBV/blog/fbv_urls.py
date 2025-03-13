from django.urls import path
from blog import views as blog_views

app_name = 'fb'

urlpatterns = [
    # FBV blog
    path('', blog_views.blog_list, name = 'list'),
    path('<int:pk>/', blog_views.blog_detail, name = 'detail'),
    path('create/', blog_views.blog_create, name = 'create'),
    path('<int:pk>/update/',blog_views.blog_update, name = 'update'),
    path('<int:pk>/delete/', blog_views.blog_delete, name = 'delete'),
]
