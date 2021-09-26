from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    tasksName = models.CharField(max_length=250,blank=True)
    taskDescription = models.CharField(max_length=1000 ,blank=True)

    def __str__(self):
        return self.user.username


