from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.MyOwnView.as_view(), name = 'home'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)