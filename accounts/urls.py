from re import template
from django.shortcuts import redirect
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import choseTask , profile, deleteProject, deleteTask, adminActivateProjects

app_name = "accounts"

urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path("availabletask", choseTask, name="chosentask"),
    path("project/<id>", deleteProject, name="deleteproject"),
    path("task/<id>", deleteTask, name="deletetask"),
    path("projectstatus/<id>", adminActivateProjects, name="projectstatus"),
]