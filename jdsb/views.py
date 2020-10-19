from django.shortcuts import render
import gspread
from rest_framework.response import Response
import json
from rest_framework.views import APIView
from services.googleSheets import googleSheetService

# Create your views here.
class getResources(APIView):
    def get(self, request):
        sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1KJCyQz0yrwdaH7hR_Yc61txUHECPT1MW1TDhnCHFoM4/edit#gid=0")
        responseData = sheet.worksheet("responses").get_all_values()
        return Response(responseData)

class getEvents(APIView):
    def get(self, request):
        sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1KJCyQz0yrwdaH7hR_Yc61txUHECPT1MW1TDhnCHFoM4/edit#gid=0")
        responseData = sheet.worksheet("events").get_all_values()
        return Response(responseData)