from django.shortcuts import render
from rest_framework.response import Response
import json
from rest_framework.views import APIView
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
from .sendMail import sendBlogEmail
import ast

class travelBlog(APIView):
    def get(self, request):
        return Response({"response":'whatsgood?'})

    def post(self, request):
        client = gspread.authorize(creds)
        client.login()
        sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1B8TWr_Pf5Z34UopHmsUSGhMT0Nmhxg5-OYj_1_sTepM/")
        emailList = sheet.worksheet('emailList')
        email = request.data['email']
        values_list = emailList.col_values(1)
        nextRow = len(values_list)+1
        emailList.update_cell(nextRow,1,email)
        return Response({"response":len(values_list)})

class blogMail(APIView):
    def get(self, request):
        client = gspread.authorize(creds)
        client.login()
        sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1B8TWr_Pf5Z34UopHmsUSGhMT0Nmhxg5-OYj_1_sTepM/")
        emailList = sheet.worksheet('emailList')
        values_list = emailList.col_values(1)
        [sendBlogEmail(email) for email in values_list]

        return Response({"response":values_list})
