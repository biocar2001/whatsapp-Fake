"""
whatsappfake URL Configuration

URLS of test application

"""
from django.conf.urls import include, url
from django.contrib import admin
# Add this import
from django.contrib.auth import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^whatsapp/', include('whatsapp.urls' ,namespace='whatsapp'), name="root"),
  ]
