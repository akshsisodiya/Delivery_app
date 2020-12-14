from django.shortcuts import render

def index(request):
    return render(request,'index.html',{'active_class':'home'})

def login(request):
    return render(request,'login.html')

def about_us(request):
    return render(request, 'about_us.html')