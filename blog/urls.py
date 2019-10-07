from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path('post/new/', views.new_post, name='new_post'),
    path('post/tag/new', views.new_tag, name='new_tag'),
    path('post/<slug:slug>/comment/new', views.add_new_comment, name="new_comment"),
    path('<slug:slug>/', views.PostDetail.as_view(), name ='post_detail'),
    path('<slug:slug>/edit', views.PostUpdateView.as_view(), name='edit_post')
]
