from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import models as user_model
from django.core.serializers import serialize
import json


class Friend(models.Model):
    person = models.OneToOneField(User, on_delete=models.CASCADE, related_name='person')
    friends = models.ManyToManyField(User)

    def __str__(self):
        return str(self.person)

class UserDetail(models.Model):
    # field = ('first_name','last_name','username', 'email', 'address1', 'address2', 'city, 'state', 'zip', 'country')
    username = models.ForeignKey(User, on_delete = models.CASCADE, null =False)
    number1 = models.IntegerField(null=False, unique=True)
    number2 = models.IntegerField(null=True, blank=True)
    address1 = models.CharField(max_length=120,null=True)
    address2 = models.CharField(max_length=120,null=True)
    city = models.CharField(max_length=50,null=True)
    state = models.CharField(max_length=50,null=True)
    zip = models.IntegerField(null=True)
    country = models.CharField(max_length=50,null=True)
    friends = models.ForeignKey(Friend, on_delete = models.CASCADE, null=True),

    def __str__(self):
        return str(self.username)

# Status Choices for Delivery
STATUS_CHOICES = (
    ("1", "Request Sent"), # request sent by sender
    ("2", "Request Accepted"), # request accepted by delivery boy
    ("3", "Request Declined"), # request declined
    ("4", "Delivery Pending"), # parcel picked up and out for delivery
    ("5", "Delivery Canceled"), # delivery canceled
    ("6", "Delivered") # parcel successfully delivered
)

class ParcelDelivery(models.Model):
    username = models.ForeignKey(User, on_delete = models.CASCADE)
    s_full_name = models.CharField(max_length=120)
    s_number1 = models.IntegerField()
    s_number2 = models.IntegerField(null=True, blank=True)
    s_address1 = models.CharField(max_length=120,null=True)
    s_address2 = models.CharField(max_length=120,null=True)
    s_city = models.CharField(max_length=50,null=True)
    s_state = models.CharField(max_length=50,null=True)
    s_zip = models.IntegerField(null=True)
    s_country = models.CharField(max_length=50, null=True)
    r_full_name = models.CharField(max_length=120)
    r_number1 = models.IntegerField()
    r_number2 = models.IntegerField(null=True, blank=True)
    r_address1 = models.CharField(max_length=120,null=True)
    r_address2 = models.CharField(max_length=120,null=True)
    r_city = models.CharField(max_length=50,null=True)
    r_state = models.CharField(max_length=50,null=True)
    r_zip = models.IntegerField(null=True)
    r_country = models.CharField(max_length=50,null=True)
    weight = models.CharField(max_length=150, null=True)
    height = models.CharField(max_length=150, null=True)
    width = models.CharField(max_length=150, null=True)
    description = models.TextField(null=True)
    time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=1)

    all_fields = ['username', 's_full_name', 's_number1', 's_number2', 's_address1', 's_address2',
                  's_city', 's_state', 's_zip', 's_country', 'r_full_name', 'r_number1', 'r_number2',
                  'r_address1', 'r_address2', 'r_city', 'r_state', 'r_zip', 'r_country', 'weight', 'height',
                  'width', 'description', 'time', 'status']

    def __str__(self):
        return str(self.pk)

    class Details():
        def __init__(self, user=None):
            self.user = user

        def seriazed_object(self, obj, max_data, pageno):
            count = obj.count()
            obj = obj[::-1]
            if max_data>0:
                obj = obj[max_data*(pageno-1):max_data]
            orders = serialize('json', obj)
            return [count, json.loads(orders)]

        def all_orders_details(self, max_data=0, pageno=1):
            total_orders = ParcelDelivery.objects.filter(username = self.user) # Object of model (Parcel Delivery), for all orders
            count, orders = self.seriazed_object(total_orders, max_data, pageno) # Empty array for dictionary of total objects
            return {'count' : count, 'orders' : orders}

        def active_orders_details(self, max_data=0, pageno=1):
            active_orders = ParcelDelivery.objects.filter(username = self.user, status__in = [1,2,3,4])
            count, orders = self.seriazed_object(active_orders, max_data, pageno)
            return {'count':count, 'orders': orders}

        def delivered_orders_details(self, max_data=0, pageno=1):
            delivered_orders = ParcelDelivery.objects.filter(username = self.user, status = 6)
            count, orders = self.seriazed_object(delivered_orders, max_data, pageno)
            return {'count': count, 'orders': orders}

        def search(self, request, max_data=10, include_delivered=False):
            try:
                pageno = request.GET['pageno']
            except:
                pageno = 1

            # check is request is with query or without query
            obj = self.get_searchable_object(include_delivered)
            try:
                query = request.GET['query']
                result = self.query_search(obj, query)
            except:
                result = obj
            count, orders = self.seriazed_object(result, max_data, pageno)
            return {'count': count, 'orders': orders}

        def get_searchable_object(self,include_delivered):
            if self.user and include_delivered: #if a user exist and include delivered true
                obj = ParcelDelivery.objects.filter(username=self.user)
            elif self.user: # if user exist but include delivered false
                obj = ParcelDelivery.objects.filter(username=self.user, status__in=[1,2,3,4])
            elif include_delivered:#if user not extst and include delivered true
                obj = ParcelDelivery.objects.all()
            else: # if user and include delivered both false
                obj = ParcelDelivery.objects.filter(status__in = [1,2,3,4])

            return obj

        def query_search(self, obj, query):
            try:
                query = int(query)
                return obj.filter(pk=query)
            except:
                result = obj.filter(r_full_name__icontains=query).filter(s_full_name__icontaines=query)
                return result