from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Record

# Create your views here.

def home(request):
    records = Record.objects.all()
    if request.method =='Post':
        return render(request, 'home.html',{})
    else:
        return render(request, 'home.html',{'records':records})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "로그인 성공")
            return redirect('home')
        else:
            messages.success(request, "아이디 혹은 비밀번호가 틀렸습니다.")
    return render(request, 'login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request, "로그아웃 완료")
    return redirect('home')