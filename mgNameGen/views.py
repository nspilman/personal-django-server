from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import random
from .nameGen import people
from .models import Image
from django.conf import settings

class MyOwnView(APIView):
    def get(self, request):
        mediaRoot = settings.MEDIA_URL
        domain = 'http://localhost:8000'
        images = Image.objects.all()
        imageArray = [domain + mediaRoot + image.filename() for image in images]
        num1 = random.randint(0,100)
        num2 = random.randint(0,100)
        personIndex = random.randint(0,len(people)) - 1
        person = people[personIndex]
        filename = images[0].filename()
        return Response({'result': num1 * num2,'person':person,'name':images[0].name,'imagePath':domain + mediaRoot + filename,'images':imageArray})
    
    def post(self,request):
        return Response({'response':'Whazgoooood?!'})
# Create your views here.
