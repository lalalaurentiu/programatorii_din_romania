from django.shortcuts import get_object_or_404, redirect, render
from home.models import Tasks
from accounts.models import UserProfile
from django.contrib import messages
from home.models import UserPost
from home.form import Task, UploadFiles
from django.contrib.auth.decorators import login_required
from .forms import ProjectStatus

@login_required
def profile(request):
    template =  "profile.html"
    userProfile = UserProfile.objects.filter(user_id=request.user.id)
    uploadProjects = UserPost.objects.filter(author_id = request.user.id)
    uploadFileForm = UploadFiles()
    taskForm = Task()
    availableProjects = UserPost.objects.filter(status="In asteptare")
    projectStatusForm = ProjectStatus()
    context = {
        "userProfile":userProfile,
        "projects":uploadProjects,
        "uploadfileform":uploadFileForm,
        "taskform":taskForm,
        "availableProjects":availableProjects,
        "projectStatusForm": projectStatusForm
    }
    return render(request, template, context)

@login_required
def choseTask(request):
    if request.method == "POST":
        task = Tasks.objects.filter(id=request.POST.get("task"))
        availableTask =  get_object_or_404(task, id=request.POST.get("task"))
        user = request.user.id
        UserProfile.objects.create(tasksName =availableTask.task ,taskDescription=availableTask.sescription, user_id = user,taskId=availableTask.id)
        task.update(available=False)
        messages.success(request, "Task Adaugat cu succes")
        return redirect("/")
    else:
        return

@login_required
def deleteProject(request, id):
    if request.method == "POST":
        projects = UserPost.objects.get(id=id)
        projects.delete()
        messages.success(request, "Proiectul dumneavoastra a fost sters")
        return redirect("/")

@login_required
def deleteTask(request, id):
    if request.method == "POST":
        task = UserProfile.objects.get(id=id)
        avaliableTask = Tasks.objects.filter(id=task.taskId)
        avaliableTask.update(available=True)
        task.delete()
        messages.success(request, "Taskul a fost sters")
        return redirect("/")

def adminActivateProjects(request, id):
    if request.method =="POST":
        # id = request.GET.get("id_project")
        print(id)
        project = UserPost.objects.filter(id=id)
        form = ProjectStatus(request.POST)
        if form.is_valid():
            status = form.cleaned_data["status"]
            print(status)
            project.update(status=status)
            messages.success(request, "Proiectul a fost actualizat")
            return redirect("/")
    else:
        return
        



