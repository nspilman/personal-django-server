from django.shortcuts import render
from rest_framework.response import Response
import json
from rest_framework.views import APIView
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('googleSheets/weddingWebsite.json', scope)

sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1IZwNQYnYAdf2Efo5YlxaMZDs3e1qtVaJge4H7KoUQH0")
guestList = sheet.worksheet("Guestlist")
sh = sheet.worksheet("spreadsheetSubmit")

#columns

groupCol = 10
firstNameCol = 2
lastNameCol = 3
emailCol = 6

def loginLog(group):
    sh.update_cell(1, 1, group + " has logged in")

# Create your views here.

class MyOwnView(APIView):
    def get(self, request):
        return Response({"response":'whatsgood?'})

    def post(self, request):
        client = gspread.authorize(creds)
        submitGroup = request.data['group']
        submitName = request.data['firstname']
        submitFunction = request.data['function'] 
        peopleArray = [
            {
                "group":submitGroup,
                "firstName":guestList.cell(person.row,firstNameCol).value,
                "lastName":guestList.cell(person.row,lastNameCol).value,
                "row":person.row, 
                "col":person.col
                } 
                for person in guestList.findall(submitGroup) 
                if person.col == groupCol 
                ]

        group = guestList.findall(submitGroup)
        if submitFunction == "login":
            loginLog(submitGroup)
        return Response({"response":peopleArray})
