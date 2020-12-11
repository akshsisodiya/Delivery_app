from django.shortcuts import render, HttpResponse, redirect, Http404
from .forms import CreateUserForm
from django.contrib.auth.models import auth
from django.contrib.auth import login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='/user/login')
def index(request):
    return render(request, 'user_index.html')

def login_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST['user_id']
        password = request.POST['password']
        check = auth.authenticate(request, username=username, password=password)
        if check is not None:
            login(request,check)
            return redirect('index')
        else:
            messages.error(request, 'Jab tujhe wrong credentials daalne the to login pe click kiya hi kyu?')
    return render(request, 'login.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                return redirect('index')
        return render(request, 'registration_form.html', {'form':form})

def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')
    else:
        raise Http404("not exist")