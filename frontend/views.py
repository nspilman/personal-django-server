from django.shortcuts import render, redirect, get_object_or_404

def index(request):
    return render(request,'frontend/index.html')

# Create your views here.
