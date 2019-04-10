from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth import authenticate
import base64
from django.contrib.auth.decorators import login_required

def index(request):
    request.session['Hello'] = 'Hey'
    return render(request,'frontend/index.html')

def person(request,username):
    return render(request,'frontend/person.html',{'username':username})

@login_required(login_url="/frontend/login")
def event(request,event):
    return render(request,'frontend/event.html',{'event':event})

def newevent(request):
    return render(request,'frontend/newevent.html')

def login(request):
    if 'HTTP_AUTHORIZATION' in request.META:
        auth = request.META['HTTP_AUTHORIZATION'].split()
        if len(auth) == 2:
            if auth[0].lower() == "basic":
                username,password = base64.b64decode(auth[1]).decode('utf-8').split(":",1)
                user = authenticate(username=username, password=password)
                if user is not None:
                    return redirect('/frontend/')
                
    # otherwise ask for authentification
    response = HttpResponse("")
    response.status_code = 401
    response['WWW-Authenticate'] = 'Basic realm="restricted area"'
    return response
    