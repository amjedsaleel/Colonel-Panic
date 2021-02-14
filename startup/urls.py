# Django
from django.urls import path

# local Django
from . import views

app_name = 'startup'

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('<str:id>/profile', views.profile, name='profile')
]

