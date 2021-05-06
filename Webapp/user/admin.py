from django.contrib import admin
from .models import UserDetail,ParcelDelivery, Friend
# Register your models here.
class ParcelDeliveryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username', 'status')

admin.site.register(UserDetail)
admin.site.register(ParcelDelivery, ParcelDeliveryAdmin)
admin.site.register(Friend)