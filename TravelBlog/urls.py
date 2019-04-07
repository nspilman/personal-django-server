from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.travelBlog.as_view(), name = 'home'),
    path('comments', views.blogMail.as_view(), name = 'blog'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)