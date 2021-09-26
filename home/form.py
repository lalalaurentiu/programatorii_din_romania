from django import forms
from django.db.models import fields
from django.forms.fields import ChoiceField
from django.utils.regex_helper import Choice
from .models import Tasks, UserPost


class Task(forms.ModelForm):
    task = forms.CharField(label="Nume task")
    description = forms.CharField(label ="Descriere" ,widget=forms.Textarea)

    class Meta:
        model = Tasks
        fields = ["task", "description"]

class UploadFiles(forms.ModelForm):
    # title =  forms.CharField("titlu")
    fileHtml = forms.FileField(label="Incarca un fisier HTML", required=False )
    fileCss = forms.FileField(label="Incarca un fisier CSS",required=False)
    fileJs = forms.FileField(label="Incarca un fisier JS",required=False)
    slug = forms.SlugField() 

    class Meta:
        model = UserPost
        fields = ["fileHtml", "fileCss", "fileJs", "slug"]