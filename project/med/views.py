from django.shortcuts import render, redirect
from django.forms.models import model_to_dict
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

def getData(request):
    if request.user and request.user.is_authenticated and request.GET.get('user'):
        #user = request.GET.get('user') # Users can now access eachothers data, by using each others ids.
        user = request.user.id # patch 1: Use request.user.id instead
        records = Records.objects.filter(user=user)
        records_data = [model_to_dict(record) for record in records]
        request.session['records'] = records_data
        return redirect('/')
    return render(request, 'med/index.html')
    
def home_view(request):
    if request.user and request.user.is_authenticated: 
        records = request.session.get('records', [])
        print(records)
        return render(request, 'med/data.html', {'records': records}) 
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
