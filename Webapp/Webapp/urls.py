from django.contrib import admin
from django.urls import path,include
from .views import index, about_us
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about-us/', about_us,name='about-us'),
    path('', index, name='index'),
    path('user/',include('user.urls')),
    path('accounts/', include('allauth.urls')),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
