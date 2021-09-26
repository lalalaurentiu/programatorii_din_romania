
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect
from accounts.forms import SignUpForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login


def register(request):
    signUpForm = SignUpForm(request.POST)
    if signUpForm.is_valid():
        signUpForm.save()
        messages.success(request, "Contul a fost creat cu succes")
    else:
        signUpForm = SignUpForm()

    return {"signUpForm":signUpForm}
    

def user_login(request):
    loginForm = LoginForm(request.POST)
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username)
        user = authenticate(request, username=username, password=password)
        if user is None:
            
            messages.warning(request, "Username sau parola incorecta")
        else:
            messages.success(request, "V-ati conectat cu succes")
            login(request, user)
        
    else:
        loginForm = LoginForm()
    return {"loginForm":loginForm}