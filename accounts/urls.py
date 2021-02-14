# Django
from django.urls import path

# local Django
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register', views.register, name='register'),
    # path('register_individual', views.register_individual, name='register_individual')
    path('login', views.login, name='login')
]
