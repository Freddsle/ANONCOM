from django.urls import path
from . import views
from .views import (PostListView,
                    PostAnonListView,
                    PostDetailView,
                    PostCreateView,
                    PostCreateAnonView,
                    PostUpdateView,
                    PostDeleteView,
                    UserPostListView)

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('anon-posts/', PostAnonListView.as_view(), name='anon-posts'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/new-anon/', PostCreateAnonView.as_view(), name='post-create-anon'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
]
