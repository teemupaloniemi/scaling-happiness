from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('med.urls')),
    path('admin/', admin.site.urls),
]
