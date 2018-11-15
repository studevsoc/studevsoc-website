from django.url import path,include
from django.view.generic import ListView, DetailView
from blog.models import post

urlpatterns = [
    path('',ListView.as_view(queryser = post.objects.all().order_by("-date")[:25], tempalte_name="blog/blog.html"))
    path(r'(?P<pk>\d+)$',DetailView.as_view(model=post,template_name='blog/post.html'))
]
