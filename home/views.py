from django.shortcuts import get_object_or_404, redirect, render
from .models import UserPost, Tasks
from .form import Task, UploadFiles
from django.contrib import messages
from django.views.decorators.clickjacking import  xframe_options_sameorigin
from .validations import verifyFile
from django.contrib.auth.decorators import login_required



def homePostView(request):
    template_name = "home/home.html"
    task = Tasks.objects.filter(available=True)
    userPost = UserPost.objects.all()
    taskForm = Task()
    uploadFileForm = UploadFiles()
    context =  {
        "task":task,
        "userpost":userPost,
        "taskform":taskForm,
        "uploadfileform":uploadFileForm,
    }
    return render(request, template_name, context)

@login_required
def taskPost(request):
    taskForm = Task(request.POST)
    if taskForm .is_valid():
        task = request.POST.get("task")
        description = request.POST.get("description")
        Tasks.objects.create(task = task, sescription = description)
        messages.success(request, "Task adaugat cu succes")
    return redirect('/')

@login_required
def saveProjects(request):
    if request.method == "POST":
        request_html_file = request.FILES['fileHtml'] if 'fileHtml' in request.FILES else None
        request_css_file = request.FILES['fileCss'] if 'fileCss' in request.FILES else None
        request_Js_file = request.FILES['fileJs'] if 'fileJs' in request.FILES else None

        dataHtml = verifyFile(request_html_file, ".html$")
        datCss = verifyFile(request_css_file, ".css$")
        dataJs = verifyFile(request_Js_file, ".js$")

        title = request.POST.get("slug")
        UserPost.objects.create(post_html = dataHtml, post_css = datCss, post_js =dataJs, slug=title, author_id = request.user.id)
        messages.success(request, "Fisier salvat")
    return redirect('/')



@xframe_options_sameorigin
def projects(request, slug = None):
    template_name = "home/project.html"
    projects = UserPost.objects.all()
    project_name = None
    
    if slug:
        project_name = get_object_or_404(projects, slug = slug)
        project = projects.filter(slug =  slug)
        context = {
        "projects":project
        }
        return render(request, template_name, context)