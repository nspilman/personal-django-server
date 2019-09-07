from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.simple, name = 'stripe'),
    path('donate/<amount>', views.donate, name = 'stripe'),
]