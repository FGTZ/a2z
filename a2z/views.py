from django.shortcuts import render, redirect
from . import models
from .forms import UserForm

# Create your views here.
def index(request):
    pass
    return render(request, 'login/index.html')

def login(request):
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "Please check your input!"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    return redirect('/index/')
                else:
                    message = "Incorrect password!"
            except:
                message = "User Email doesn't exist!"
        return render(request, 'login/login.html', locals())

    login_form = UserForm()
    return render(request, 'login/login.html', locals())

def logout(request):
    pass
    return redirect('/index/')