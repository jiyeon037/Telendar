from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from .models import *

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            auth.login(request, user) # 회원가입 후 자동 로그인
            return redirect('login')
    return render(request, 'signup.html')

def login(request):
    # 해당 쿠키에 값이 없을 경우 None을 return 한다.
    if request.COOKIES.get('username') is not None:
        username = request.COOKIES.get('username')
        password = request.COOKIES.get('password')
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("cal:calendar")  
        else:
            return render(request, "login.html")

    elif request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(request, username=username, password=password)

            if user is not None: # 유저가 존재하는 회원이라면
                auth.login(request, user)
                response = HttpResponseRedirect(reverse('cal:calendar'))
                response.set_cookie('username', username)
                response.set_cookie('password', password)
                return response
            else:
                return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

def logout(request):
    response = redirect('login')
    response.delete_cookie('username')
    response.delete_cookie('password')
    auth.logout(request)
    return response