from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.models import User
from med.models import Records

def add(request):
    if request.method == "POST":
        Records.objects.create(user=request.user, body=request.POST.get('body'))
    return redirect('/')

def clear(request):
    User.objects.all().delete()
    return redirect('/')

def home_view(request):
    if request.user and not request.user.is_anonymous:
        print(request.user)
        records = Records.objects.filter(user=request.user)
        return render(request, 'med/data.html', {"records": records})
    return render(request, 'med/index.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            django_login(request, user)
    return redirect('/')

def logout(request):
    django_logout(request)
    return redirect('/')

def create_users(request):
    User.objects.create_user(username='bob', password='squarepants')
    print("created bob squarepants")
    User.objects.create_user(username='alice', password='redqueen')
    print("created alice redqueen")
    User.objects.create_user(username='test', password='test')
    print("created test test")
    return redirect('/')
