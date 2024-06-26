from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('add/', views.add, name='add'),
    path('getData/', views.getData, name='getData'),
    path('log/', views.log, name='log'),
    path('clear/', views.clear, name='clear'),
    path('create/', views.create_users, name='create'),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
]


