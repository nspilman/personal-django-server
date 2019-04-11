from django.shortcuts import render
from django.db.models import Q
from django.forms.models import model_to_dict
from django.contrib.auth.models import User
from rest_framework.response import Response
import json
from rest_framework.views import APIView
from .models import Event, Eventprofile
from .mockup_tools import fakeuser, fakeaddress
import random
from django.contrib.auth import authenticate, login


class AllEvents(APIView):  
    def get(self,request):
        events = [{
            'id':event.id,
            'name':event.name,
            'created_user':str(event.created_user), 
            'startdate':event.startdate,
            'address':event.address,
            'enddate':event.enddate,
            'starttime':event.starttime,
            'endtime':event.endtime
            } 
            for event in Event.objects.all()]
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
        event = Event(name=name,created_user=created_user,startdate = startdate, enddate = enddate, starttime = starttime,endtime = endtime, address=fakeaddress())
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
        username = request.data['username']
        user = User.objects.create_user(username, 'lennon@thebeatles.com', 'johnpassword')
        user.eventprofile.event_user = True
        user.save()
        return Response(user_data)

class Signups(APIView):
    def get(self,request, user = ""):
        if user == "":
            events = [event.id for event in Event.objects.all()]
        else:
            try:
                events = [{
                    'id':event.id,
                    'name':event.name,
                    'created_user':str(event.created_user), 
                    'address':event.address,
                    'startdate':event.startdate,
                    'enddate':event.enddate,
                    'starttime':event.starttime,
                    'endtime':event.endtime
            } for event in Event.objects.filter(attendees__username = user)]
            except:
                events = []
        return Response(events)

    def post(self,request):
        data = request.data
        event = Event.objects.get(id = data['event_id'])
        user = User.objects.get(username = data['username'])
        event.attendees.add(user)
        event.save()
        # user = User.objects.create_user('testUserOne', 'lennon@thebeatles.com', 'johnpassword')
        return Response({'attendees':event.id})

class eventSignups(APIView):
    def get(self,request, event = ""):
        if event == "":
            events = [event.id for event in Event.objects.all()]
        else:
                eventObj = Event.objects.get(id = event)
                event = {
                    'id':eventObj.id,
                    'name':eventObj.name,
                    'created_user':str(eventObj.created_user), 
                    'address':eventObj.address,
                    'startdate':eventObj.startdate,
                    'enddate':eventObj.enddate,
                    'starttime':eventObj.starttime,
                    'endtime':eventObj.endtime,
            } 
                attendees = [user.username for user in eventObj.attendees.all()]
        return Response({'event_info':event,'attendees':attendees})


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
                events = [{
                    'id':event.id,
                    'name':event.name,
                    'created_user':str(event.created_user), 
                    'address':event.address,
                    'startdate':event.startdate,
                    'enddate':event.enddate,
                    'starttime':event.starttime,
                    'endtime':event.endtime,
                    } for event in Event.objects.filter(created_user__username = user)]
            except:
                events = []
        return Response(events)

class Mockup(APIView):
    def post(self,request):
        data = request.data
        number = data['number']
        function = data['function']

        if function == 'user':
            for i in range(0,number):
                user_data = fakeuser()
                user = User.objects.create_user(user_data['username'], user_data['email'], user_data['password'])
                user.eventprofile.event_user = True
                user.save()
            return Response({'200':f'created {number} user(s)'})

        if function == 'event':
            for i in range(0,number):
                user_index = random.randint(0,len(User.objects.all())-1)
                created_user = User.objects.all()[user_index]
                event = Event(
                    name=created_user.username + "'s awesome event",
                    created_user=created_user,
                    address = fakeaddress(),
                    startdate="2019-01-01",
                    enddate="2019-01-01",
                    starttime="12:00",
                    endtime="13:00"
                    )
                event.save()
            return Response({'200':f'created {number} event(s)'})
        if function == 'attend':
            for i in range(0,number):
                user_index = random.randint(0,len(User.objects.all())-1)
                user = User.objects.all()[user_index]
                event_index = random.randint(0,len(Event.objects.all())-1)
                event = Event.objects.all()[event_index]
                event.attendees.add(user)
                event.save()
            return Response({'200':f'signed up {number} person(s) for an event'})
        if function == 'burnitdown':
            # try:
                if data['burnitdown']=="burn":
                    User.objects.filter(eventprofile__event_user=True).delete()
                    Event.objects.all().delete()
                else:
                    return Response({'401':'Wrong Password'})
                return Response({'200':"There's nothing left"})
            # except:
                # return Response({'401':'Missing stuff, man'})

class Login_Class(APIView):
    def post(self,request):
        # return Response(request.data)
        username = request.data['username']
        password = request.data['password']    
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'200':"You're logged in!"})
        else:
            return Response({'401':'We dont know who you are, bruv'})

    def get(self,request):
        return Response({'logged_in':request.user.username})

