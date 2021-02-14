# Django
from django.urls import path

# local Django
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup', views.register, name='register'),
    path('login', views.login, name='login')
]
