from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.PostView.as_view(), name = 'postComment'),
    path('getComments/<blogpost>', views.GetView.as_view(), name = 'getComments'),
]