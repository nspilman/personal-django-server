from django.shortcuts import render
from .models import Post
from rest_framework.views import APIView
from django.conf import settings
from rest_framework.response import Response
import json

class MyOwnView(APIView):
    def get(self, request):
        mediaRoot = settings.MEDIA_URL
        domain = 'http://localhost:8000'
        posts = Post.objects.all()
        responseArray = [{'title':post.title,'image':domain + mediaRoot + post.filename(), 'content':post.content} for post in posts]
        return Response({"response":responseArray})
    
    def post(self,request):
        return Response({'response':request.body})
# Create your views here.
