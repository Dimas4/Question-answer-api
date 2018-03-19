from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Message(models.Model):
    user = models.CharField(max_length=50)
    message = models.TextField()
    answer = models.TextField()
    data_new = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user