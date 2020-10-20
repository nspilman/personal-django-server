from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('business/', views.Businesses.as_view()),
    path('business/<int:pk>/', views.BusinessRecord.as_view()),
    path('offering/', views.Offerings.as_view()),
    path('offering/<int:pk>/', views.OfferingRecord.as_view()),
    path('customer/', views.Customers.as_view()),
    path('customer/<int:pk>/', views.CustomerRecord.as_view()),
    path('order/', views.Orders.as_view()),
    path('order/<int:pk>/', views.OrderRecord.as_view()),
]