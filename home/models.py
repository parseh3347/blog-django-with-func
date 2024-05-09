from django.db import models
from django.utils import timezone
# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now)


