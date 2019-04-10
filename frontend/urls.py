from django.urls import path
from django.conf.urls import include

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('person/<username>',views.person, name = "person"),
    path('event/<event>',views.event,name='event'),
    path('newevent',views.newevent,name='newevent'),
    path('login/',views.login,name='login')
]