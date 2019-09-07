from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse
import json
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

# Create your views here.

class LoginView(APIView):
    # authentication_classes = (SessionAuthentication, BasicAuthentication)
    # permission_classes = (IsAuthenticated,)
    def post(self, request):
            # permission_classes = (IsAuthenticated,)
            print(request.data)
            username = request.data['username']
            password = request.data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
             # the password verified for the user
                if user.is_active:
                    login(request, user)
                    return JsonResponse({'response':'200','message':'you good, bro'})
                else:
                    return JsonResponse({'response':'401','message':'uhm...?'})
            else:
                    return JsonResponse({'response':'403','message':'Dunno who you are tho...?'})


@login_required(login_url='./loginFailed')
def logginSuccess(request):
    return JsonResponse({'response':'200','message':'You good, man!!'})

def loginFailed(request):
    return JsonResponse({'response':'401','message':'Be gone, THOT!!'})


