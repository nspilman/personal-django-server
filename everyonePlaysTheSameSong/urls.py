from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('state', views.CurrentState.as_view(), name = 'State'),
    path('', views.RoundsMetaData.as_view(), name = 'RoundsMetaData'),
    path('<roundId>', views.RoundsMetaData.as_view(), name = 'RoundsMetaData'),
]