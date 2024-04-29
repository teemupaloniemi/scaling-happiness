from django.db import models
from django.conf import settings  

class Records(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='records')
    body = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
