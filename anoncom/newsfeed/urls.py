from django.urls import path

from . import views

app_name = 'newsfeed'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),   
    path('new/', views.PostCreateView.as_view(), name='post_new'),
    path('<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
]