from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('template/', views.hello_template, name='hello_template'),
    path('single/', views.single_page, name='single_page'),
]