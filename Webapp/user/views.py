from django.shortcuts import render, HttpResponse, redirect

def index(request):
    pass

def login(request):
    user_id = request.POST['user_id']
    password = request.POST['password']

    if user_id == 'admin' and password == 'admin':
        return HttpResponse('hello')

    else:
        return redirect('/login')

def register(request):
    pass