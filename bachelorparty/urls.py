from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name = 'stripe'),
    path('loggedIn/', views.logginSuccess, name = 'stripe'),
    path('loginFailed/', views.loginFailed, name = 'stripe'),
]