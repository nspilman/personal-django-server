from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('business/', views.Businesses.as_view()),
    path('offering/', views.Offerings.as_view()),
    path('customer/', views.Customers.as_view()),
    path('order/', views.Orders.as_view()),
]