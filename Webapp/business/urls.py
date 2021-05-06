from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='business_index'),
    path('total-delivery/', views.total_delivery, name='total_delivery'),
    path('pending-delivery/', views.pending_delivery, name='pending_delivery'),
    path('pending-requests/', views.pending_requests, name='pending_requests'),
    path('search/', views.search, name='business_search'),
    path('chat/', views.chat, name='business_chat'),
    path('order-detail/<int:id>/', views.order_detail, name='order_detail'),
    path('change-status/', views.change_status, name='change_status'),
    path('mass-change-status/', views.mass_change_status, name='mass_change_status'),
]