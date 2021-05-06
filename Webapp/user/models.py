from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import models as user_model


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
    friends = models.ForeignKey(Friend, on_delete = models.CASCADE, null=True)

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

    def __str__(self):
        return str(self.pk)