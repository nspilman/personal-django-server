from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.weddingDocs.as_view(), name = 'gSheet'),
    path('/blog', views.travelBlog.as_view(), name = 'blog'),
    path('/blogMail', views.blogMail.as_view(), name = 'blogMail'),
]