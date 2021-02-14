# Django
from django.urls import path

# local Django
from . import views

app_name = 'startup'

urlpatterns = [
    path('', views.startup, name='startup')
]
