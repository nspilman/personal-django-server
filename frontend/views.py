from django.shortcuts import render, redirect, get_object_or_404

def index(request):
    return render(request,'frontend/index.html')

def person(request,username):
    return render(request,'frontend/person.html',{'username':username})

def event(request,event):
    return render(request,'frontend/event.html',{'event':event})


# Create your views here.
