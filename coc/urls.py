from django.urls import path

from . import views

urlpatterns = [
    path('', views.coc_list, name="coc_list"),
]
