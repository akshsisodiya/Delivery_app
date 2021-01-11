from django.contrib import admin
from .models import UserDetail,ParcelDelivery, Friend
# Register your models here.
admin.site.register(UserDetail)
admin.site.register(ParcelDelivery)
admin.site.register(Friend)