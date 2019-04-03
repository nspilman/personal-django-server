from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from django.forms.models import model_to_dict
from .sendMail import sendEmail
from .emailInfo import email, password

class emailView(APIView):
    def post(self, request):
        data = request.data
        fromName = data['name']
        fromEmail = data['email']
        subject = data['subject']
        message = str(fromEmail) + """
        """ + str(data['message'])

        sendEmail(email,password,"nate.spilman@gmail.com",fromName + " " + fromEmail, subject, message)

        return Response({"success"})
    def get(self, request):
        return Response({'hey'})
    
# Create your views here.
