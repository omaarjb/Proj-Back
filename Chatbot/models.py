from django.db import models

# Create your models here.

class Message(models.Model):
    text = models.CharField(max_length=255)
    sender = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)