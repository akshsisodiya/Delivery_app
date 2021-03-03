from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='business_index'),
    path('total-delivery/', views.total_delivery, name='total_delivery'),
    path('panding-delivery/', views.panding_delivery, name='panding_delivery'),
    path('panding-requests/', views.panding_requests, name='panding_requests'),
    path('search/', views.search, name='business_search'),
    path('chat/', views.chat, name='business_chat'),
    path('order-detail/<int:id>/', views.order_detail, name='order_detail'),
]