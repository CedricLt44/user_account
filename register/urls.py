# register/urls.py
from django.urls import path
from . import views

app_name = 'register'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
]
