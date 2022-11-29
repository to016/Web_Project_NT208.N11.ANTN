from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegisterForm
from .models import User


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        registerForm = RegisterForm
        if form.is_valid():
            email = request.POST['email']
            if User.objects.filter(email=email):
                return render(request, 'account/register.html', { 'f' : registerForm, 'message' : 'Email is already token'})
            else:
                form.save()
                return render(request, 'account/register.html', { 'f' : registerForm, 'message' : 'Register successfully' })
        return render(request, 'account/register.html', { 'f' : registerForm, 'message' : 'Form is invalid' })
    elif request.method == 'GET':
        registerForm = RegisterForm
        return render(request, 'account/register.html', { 'f' : registerForm})

def login(request):
    return HttpResponse("login")