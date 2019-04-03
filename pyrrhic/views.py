from django.shortcuts import render
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from rest_framework.response import Response
import json
from rest_framework.views import APIView

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('googleSheets/weddingWebsite.json', scope)
client = gspread.authorize(creds)

class gsheetData(APIView):
    def get(self,request):
        client = gspread.authorize(creds)
        client.login()
        sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/17VCNwQLbkSsK0xm2Hq7LaPu1PGlR9zUOGuj5WCppLjw/edit#gid=0")
        videosData = sheet.worksheet("videos")
        videoNames = videosData.col_values(1)[1:]
        artists = videosData.col_values(2)[1:]
        yt = videosData.col_values(3)[1:]
        category = videosData.col_values(4)[1:]
        headers = videosData.row_values(1)

        data = [{headers[0]:videoNames[i],headers[1]:artists[i],headers[2]:yt[i],headers[3]:category[i],} for i in range(0,len(videoNames))]
        return Response(data)
        

        



# Create your views here.
