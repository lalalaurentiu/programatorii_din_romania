from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.urls import reverse

"""
Definirea bazei de date unde vom tine toate templateurile
"""

class Tasks(models.Model):
    task = models.CharField(max_length=500)
    sescription = models.TextField(blank=True)
    available = models.BooleanField(default=True)

class UserPost(models.Model):

    activ = "Activ"
    dezactivat = "Dezactivat"
    inAsteptare = "In asteptare"

    choicesStatus = [
        (activ, "Activ"),
        (dezactivat, "Dezactivat"),
        (inAsteptare, "In asteptare")
    ]

    author = models.ForeignKey(User, on_delete=CASCADE)
    title = models.CharField(blank=True, max_length=250)
    post_html = models.TextField(blank=True)
    post_css = models.TextField(blank=True)
    post_js = models .TextField(blank=True)
    status = models.CharField(max_length=15, choices=choicesStatus, default=inAsteptare)
    slug = models.SlugField(max_length=250, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("home:project", args=[self.slug])
