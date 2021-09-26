from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm


class SignUpForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True, label="Nume")
    email = forms.EmailField(max_length=300, required=True, label="Email")
    password = forms.CharField(widget = forms.PasswordInput(), label="Parola")
    confirmPassword = forms.CharField(widget = forms.PasswordInput(), label="Confirma parola")

    class Meta:
        model = User
        fields = ("username", "email", "password", "confirmPassword")
        widgets = {
            "password":forms.PasswordInput(),
            "confirmPassword":forms.PasswordInput(),
        }
    def save(self, commit= True):
        user = super(SignUpForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, required=True, label="Nume")
    password = forms.CharField(widget = forms.PasswordInput(), label="Parola")

    


