from . import views
from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('', PostListView.as_view(), name='index'),
    #path('user/<str:username>/', UserPostListView.as_view(), name='user_posts'),
    #path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post'),
    path('post/<int:slug>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:slug>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('about/', views.about, name='about'),
]

