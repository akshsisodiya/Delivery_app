from django.shortcuts import render

def index(request):
    return render(request, 'business/index.html')

def total_delivery(request):
    return render(request, 'business/index.html')

def panding_delivery(request):
    return render(request, 'business/index.html')

def panding_requests(request):
    return render(request, 'business/index.html')

def order_detail(request):
    return render(request, 'business/index.html')

def search(request):
    return render(request, 'business/index.html')

def chat(request):
    return render(request, 'business/index.html')