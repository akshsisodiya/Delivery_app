from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import models as user_model

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

    def __str__(self):
        return str(self.username)

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
    time = models.DateTimeField(auto_now_add=True)