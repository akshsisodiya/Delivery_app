from django.shortcuts import render, get_object_or_404, Http404, HttpResponse
from user.models import ParcelDelivery, STATUS_CHOICES
from django.core import serializers
import json

# index page
def index(request):
    total_delivery = json.loads(serializers.serialize('json', ParcelDelivery.objects.filter(status=6)))
    pending_delivery = json.loads(serializers.serialize('json', ParcelDelivery.objects.filter(status=4)))
    pending_requests = json.loads(serializers.serialize('json', ParcelDelivery.objects.filter(status=1)))
    # print(total_delivery[0]['fields'])
    total_delivery_count = len(total_delivery)
    # print(total_delivery_count)
    pending_delivery_count = len(pending_delivery)
    pending_requests_count = len(pending_requests)
    return render(request, 'business/index.html', {'data':{'total_delivery':total_delivery_count, 'pending_delivery': pending_delivery_count, 'pending_requests': pending_requests_count}})

# total parcel delivered
def total_delivery(request):
    total_delivery = json.loads(serializers.serialize('json', ParcelDelivery.objects.filter(status=6)))
    total_delivery_count = len(total_delivery)
    return render(request, 'business/index.html', {'data':total_delivery, 'count':total_delivery_count})

# parcels to be delivered
def pending_delivery(request):
    pending_delivery = json.loads(serializers.serialize('json', ParcelDelivery.objects.filter(status=4)))
    pending_collection = json.loads(serializers.serialize('json', ParcelDelivery.objects.filter(status=2)))
    pending_delivery_count = len(pending_delivery)
    return render(request, 'business/index.html', {'data_delivery':pending_delivery, 'data_collection':pending_collection, 'count':pending_delivery_count})

# pending delivery requests
def pending_requests(request):
    pending_requests = json.loads(serializers.serialize('json', ParcelDelivery.objects.filter(status=1)))
    pending_requests_count = len(pending_requests)
    return render(request, 'business/index.html', {'data':pending_requests, 'count':pending_requests_count})

# detail of individual order
def order_detail(request, id):
    detail = get_object_or_404(ParcelDelivery, pk=id)
    return render(request, 'business/index.html', {'detail':detail, 'page':'order_detail'})

# search bar function
def search(request):
    return render(request, 'business/index.html')

# chat feature
def chat(request):
    return render(request, 'business/index.html')

# change delivery status
def change_status(request):
    if request.method == 'POST':
        id = request.POST['id']
        status = request.POST['status']
        delivery = ParcelDelivery.objects.get(pk=id)
        delivery.status = status
        delivery.save()
        return HttpResponse(status=200)
    return HttpResponse(status=400)

def mass_change_status(request):
    if request.method == 'POST':
        order_ids = request.POST.getlist('orders[]')
        print(order_ids)
        status = request.POST['status']
        for order_id in order_ids:
            delivery = ParcelDelivery.objects.get(pk=order_id)
            delivery.status = status
            delivery.save()
        return HttpResponse(status=200)
    return HttpResponse(status=400)