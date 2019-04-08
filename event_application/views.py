from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
import json
from rest_framework.views import APIView
from .models import Event

class AllEvents(APIView):  
    def get(self,request):
        events = [{'name':event.name} for event in Event.objects.all()]
        return Response(events)
    
    def post(self,request):
        data = request.data
        name = data['name']
        created_user = User.objects.get(username = data['created_user'])
        try:
            startdate = data['startdate']
        except:
            startdate = ""
        try:
            enddate = data['enddate']
        except:
            enddate = ""
        try:
            starttime = data['starttime']
        except:
            starttime = ""
        try:
            endtime = data['endtime']
        except:
            endtime = ""
        event = Event(name=name,created_user=created_user,startdate = startdate, enddate = enddate, starttime = starttime,endtime = endtime)
        event.save()
        # user = User.objects.create_user('testUserOne', 'lennon@thebeatles.com', 'johnpassword')
        return Response({'response':f'new event created - {name}'})

# Create your views here.
class Users(APIView):  
    def get(self,request,user = ''):
        if user == '':
            users = [user.username for user in User.objects.all()]
        else:
            try:
                users = User.objects.get(username = user).username
            except:
                users = ''
        return Response({'hey':users})

    def post(self,request):
        user_data = request.data['body']
        # user = User.objects.create_user('testUserOne', 'lennon@thebeatles.com', 'johnpassword')
        return Response(user_data)

class Signups(APIView):
    def get(self,request, user = ""):
        if user == "":
            events = [event.id for event in Event.objects.all()]
        else:
            try:
                events = [event.id for event in Event.objects.filter(attendees__username = user)]
            except:
                events = []
        return Response({'hey':events})

    def post(self,request):
        data = request.data
        event = Event.objects.get(id = data['event_id'])
        user = User.objects.get(username = data['username'])
        event.attendees.add(user)
        event.save()
        # user = User.objects.create_user('testUserOne', 'lennon@thebeatles.com', 'johnpassword')
        return Response({'attendees':event.id})

class Remove(APIView):
    def post(self,request):
        data = request.data
        event = Event.objects.get(id = data['event_id'])
        user = User.objects.get(username = data['username'])
        event.attendees.remove(user)
        event.save()
        # user = User.objects.create_user('testUserOne', 'lennon@thebeatles.com', 'johnpassword')
        return Response({'attendees':event.id})

class CreatedBy(APIView):
    def get(self,request, user =""):
        if user == "":
            events = [event.name for event in Event.objects.all()]
        else:
            try:
                events = [event.name for event in Event.objects.filter(created_user__username = user)]
            except:
                events = []
        return Response({'hey':events})

