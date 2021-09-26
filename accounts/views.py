from django.shortcuts import get_object_or_404, redirect, render
from home.models import Tasks
from accounts.models import UserProfile
from django.contrib import messages
from home.models import UserPost
from home.form import Task, UploadFiles
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    template =  "profile.html"
    userProfile = UserProfile.objects.filter(user_id=request.user.id)
    uploadProjects = UserPost.objects.filter(author_id = request.user.id)
    uploadFileForm = UploadFiles()
    taskForm = Task()
    context = {
        "userProfile":userProfile,
        "projects":uploadProjects,
        "uploadfileform":uploadFileForm,
        "taskform":taskForm
    }
    return render(request, template, context)

@login_required
def choseTask(request):
    if request.method == "POST":
        task = Tasks.objects.filter(id=request.POST.get("task"))
        availableTask =  get_object_or_404(task, id=request.POST.get("task"))
        user = request.user.id
        print(availableTask.task, availableTask.sescription, user)
        UserProfile.objects.create(tasksName =availableTask.task ,taskDescription=availableTask.sescription, user_id = user)
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



