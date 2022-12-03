from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm, LoginForm
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
    if request.method == 'POST':
        form = LoginForm(request.POST)
        loginForm = LoginForm
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']

            check_user = User.objects.filter(email=email, password=password)
            if check_user:
                request.session['user'] = email
                request.session['uname'] = check_user[0].fullName
                return redirect('shop:product_list')
            else: # Wrong password or email;
                return render(request, 'account/login.html', { 'f' : loginForm, 'message' : 'Email or Password is wrong' })

        return render(request, 'account/login.html', { 'f' : loginForm, 'message' : 'Form is invalid' })
    elif request.method == 'GET':
        loginForm = LoginForm
        return render(request, 'account/login.html', { 'f' : loginForm})

# def home(request):
#     loginForm = LoginForm
#     if 'user' in request.session:
#         param = {'current_user': request.session['uname']}
#         return render(request, 'account/home.html', param)
#     else:
#         return render(request, 'account/login.html', { 'f' : loginForm})

def logout(request):
    loginForm = LoginForm
    try:
        del request.session['user']
    except:
        return redirect('account:login')
    return redirect('account:login')