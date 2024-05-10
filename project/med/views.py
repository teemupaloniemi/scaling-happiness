import time
from django.shortcuts import render, redirect
from django.forms.models import model_to_dict
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from med.models import Records

PATCH0 = True
PATCH1 = True
PATCH2 = True

def add(request):
    if request.method == "POST":
        Records.objects.create(user=request.user, body=request.POST.get('body'))
    return redirect('/')


def clear(request):
    User.objects.all().delete()
    return redirect('/')


def getData(request):
    if request.user and request.user.is_authenticated and request.GET.get('user'):
        user = request.GET.get('user') # Users can now access eachothers data, by using each others ids.
        if PATCH0:
            user = request.user.id # patch 0: Use request.user.id instead
        if PATCH1:
            with open('log.txt', 'a', encoding='utf-8') as log_file:
                log_file.write(f"==== {time.strftime('%m/%d/%Y', time.localtime(time.time()))} - { time.strftime('%H:%M:%S', time.localtime(time.time())) } | {request.user} requested data with user id {user} ====\n")
        records = Records.objects.filter(user=user)
        records_data = [model_to_dict(record) for record in records]
        request.session['records'] = records_data
        return redirect('/')
    if PATCH1:
        with open('log.txt', 'a', encoding='utf-8') as log_file:
            log_file.write(f"==== {time.strftime('%m/%d/%Y', time.localtime(time.time()))} - { time.strftime('%H:%M:%S', time.localtime(time.time())) } | Unauthenticated user tried to requested data ====\n") 
    return render(request, 'med/index.html')


def home_view(request):
    if request.user and request.user.is_authenticated: 
        records = request.session.get('records', [])
        return render(request, 'med/data.html', {'records': records}) 
    return render(request, 'med/index.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if PATCH1:
                with open('log.txt', 'a', encoding='utf-8') as log_file:
                    log_file.write(f"==== {time.strftime('%m/%d/%Y', time.localtime(time.time()))} - { time.strftime('%H:%M:%S', time.localtime(time.time())) } | {user} logged in ====\n")
            django_login(request, user)
            return redirect('/')
        if PATCH1:
            with open('log.txt', 'a', encoding='utf-8') as log_file:
                log_file.write(f"==== {time.strftime('%m/%d/%Y', time.localtime(time.time()))} - { time.strftime('%H:%M:%S', time.localtime(time.time())) } | Attempt to login without existing user username={username} password={password} ====\n")

    if PATCH1:
        with open('log.txt', 'a', encoding='utf-8') as log_file:
            log_file.write(f"==== {time.strftime('%m/%d/%Y', time.localtime(time.time()))} - { time.strftime('%H:%M:%S', time.localtime(time.time())) } | Login attemp with wrong method ====\n")
    return redirect('/')


def logout(request):
    if request.user and request.user.is_authenticated:
        if PATCH1:
            with open('log.txt', 'a', encoding='utf-8') as log_file:
                log_file.write(f"==== {time.strftime('%m/%d/%Y', time.localtime(time.time()))} - { time.strftime('%H:%M:%S', time.localtime(time.time())) } | {request.user} logged out ====\n")
        django_logout(request)
        return redirect('/')
    if PATCH1:
        with open('log.txt', 'a', encoding='utf-8') as log_file:
            log_file.write(f"==== {time.strftime('%m/%d/%Y', time.localtime(time.time()))} - { time.strftime('%H:%M:%S', time.localtime(time.time())) } | Unauthenticated user tied loggig out ====\n")     

    return redirect('/')


# pathc 2: helper for log tests
def isadmin(user):
    if PATCH2:
        return user.is_authenticated and user.is_staff
    return True

@login_required
@user_passes_test(isadmin, login_url='/') # patch 2: only admin is allowed to see the logs
def log(request):
    if PATCH1:
        log_data = []
        with open('log.txt', 'r', encoding='utf-8') as log_file:
            for line in log_file:
                log_data.append(line)
        return render(request, 'med/log.html', {'data': log_data})
    return redirect('/')

def create_users(request):
    User.objects.create_user(username='bob', password='squarepants')
    print("created bob squarepants")
    User.objects.create_user(username='alice', password='redqueen')
    print("created alice redqueen")
    User.objects.create_user(username='test', password='test')
    print("created test test")
 
    return redirect('/')
