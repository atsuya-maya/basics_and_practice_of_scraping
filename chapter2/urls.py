from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('_2_3', views._2_3, name='_2_3'),
    path('_2_4', views._2_4, name='_2_4'),
]