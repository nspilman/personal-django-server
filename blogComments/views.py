from django.shortcuts import render
from .models import Comment
from rest_framework.response import Response
import json
from rest_framework.views import APIView

# Create your views here.
class PostView(APIView):    
    def post(self,request):
        comment_obj = request.data
        Comment.objects.create(blog_post = comment_obj['post'],comment_text = comment_obj['text'], author = comment_obj['author'])
        return Response({'response':comment_obj})

class GetView(APIView):
    def get(self,request,blogpost):
        posts = Comment.objects.filter(blog_post = blogpost)
        postComments = [{"id":post.blog_post,"author":post.author,"text":post.comment_text,"date":post.created_at} for post in posts]
        return Response({'response':postComments})
