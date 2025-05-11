# register/views.py
from django.shortcuts import render

def login(request):
    return render(request, 'register/login.html')

def signup(request):
    return render(request, 'register/signup.html')
