from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_page , name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('send-parcel/', views.send_parcel, name='send_parcel'),
    path('requset-parcel/', views.requset_parcel, name='requset_parcel'),
    path('track-delivery/', views.requset_parcel, name='track_delivery'),
    path('profile/', views.profile, name='profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('api/check-user/', views.check_user, name='check_user'),
    path('api/get-user/', views.get_user, name='get_user'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_message.html'), name='password_reset_complete'),
    path('<str:username>/', views.user_profile_show, name='user_profile_show')
]