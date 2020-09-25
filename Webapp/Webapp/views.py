from django.shortcuts import render

def index(request):
    return render(request,'index.html',{'active_class':'home'})

def register(request):
    return render(request,'registration_form.html')