
from django.urls import path
from .views import homePostView, taskPost, saveProjects,projects

app_name = "home"

urlpatterns = [
    path('', homePostView, name="home"),
    path('task', taskPost, name="task"),
    path('save', saveProjects, name="save"),
    path("<slug:slug>", projects, name="project"),
]