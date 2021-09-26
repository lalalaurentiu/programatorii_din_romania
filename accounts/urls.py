from re import template
from django.shortcuts import redirect
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import choseTask , profile, deleteProject

app_name = "accounts"

urlpatterns = [
    # path("login/",auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path("availabletask", choseTask, name="chosentask"),
    path("<id>/", deleteProject, name="deleteproject"),

]