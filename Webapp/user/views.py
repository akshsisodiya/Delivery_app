from django.shortcuts import render, HttpResponse, redirect, Http404
from .forms import CreateUserForm
from django.contrib.auth.models import auth
from django.contrib.auth import login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import CardView

@login_required(login_url='/user/login')
def index(request):
    profile = CardView('Profile', 'aksh004.jpg', 'Goto your profile')
    send = CardView('Send', 'send.jpg', 'Quick proccess to send your parcel')
    request_p = CardView('Request parcel', 'request.jpg', 'Request something from your friendlist')
    tracking = CardView('Track Parcel', 'tracking.jpg', 'Track current location of your parcels')
    return render(request, 'user_index.html', {'data': [send,request_p,tracking,profile], 'active_class':'home'})

def profile(request):
    return render(request, 'user_profile.html')

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

# takes email for reseting password
def password_reset(request):
    return render(request, 'password_reset.html')

# shows message that email has been sent
def password_reset_done(request):
    return render(request, 'password_reset_done.html')

# takes new password
def password_reset_confirm(request):
    if request.method == 'POST':
        return redirect('password_reset_message')
    else:
        return render(request, 'password_reset_confirm.html')

# shows message that password changed
def password_reset_message(request):
    return render(request, 'password_reset_message.html')

def indexdata(obj,title,img,disc):
    obj = CardView
    obj.title = title
    obj.img = img
    obj.discription = disc
    return obj