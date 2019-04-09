from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('',views.AllEvents.as_view()),
    path('users/', views.Users.as_view()),
    #endpoint used to check if a user exists
    path('users/<user>/', views.Users.as_view()),
    path('remove/', views.Remove.as_view()),
    path('mockup/',views.Mockup.as_view()),
    #pulls events that a user is signed up for, based on username
    path('usersignups/<user>/', views.Signups.as_view()),
    path('eventsignups/<event>/', views.eventSignups.as_view()),
    #pulls events that a user created, based on username
    path('createdby/<user>/', views.CreatedBy.as_view()),
]