from django.shortcuts import render
from rest_framework.response import Response
import json
from rest_framework.views import APIView
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
from googleSheets.sendMail import sendBlogEmail
import ast
from googleSheets.creds import creds, scope, client
from jobhunt.sendMail import sendEmail
from jobhunt.emailInfo import email, password

#columns
#guestList
groupCol = 10
firstNameCol = 2
lastNameCol = 3
emailCol = 6
rsvpCol = 18
rehearsal_dinner_rsvp_col = 22
plus1Col = 23
foodCol = 24
plusOneFoodCol = 25
rsvp_note_col = 30

#loginList
llGroupCol = 1
llNameCol = 2
llDateCol = 3
llTimeCol = 4
llLastCol = 5

def loginLog(person,sh):
    lastCell = llLastRow(sh)
    time = datetime.datetime.time(datetime.datetime.now())
    date = datetime.date.today()
    sh.update_cell(lastCell, llGroupCol, person['group'])
    sh.update_cell(lastCell, llNameCol, person['lastName'])
    sh.update_cell(lastCell,llDateCol,str(date))
    sh.update_cell(lastCell,llTimeCol,str(time))
    llNextRow(sh)

def llLastRow(sh):
    try:
        lastCell = sh.find('last').row
        return lastCell + 1
    except:
        return 2

def llNextRow(sh):
    nextRow = llLastRow(sh)
    try:
        lastCell = sh.find('last')
        sh.update_cell(lastCell.row,lastCell.col, '')
    except:
        pass
    sh.update_cell(nextRow,llLastCol,"last")

# Create your views here.

class weddingDocs(APIView):
    def get(self, request):
        return Response({"response":'Success?'})

    def post(self, request):
        client = gspread.authorize(creds)
        client.login()
        sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1IZwNQYnYAdf2Efo5YlxaMZDs3e1qtVaJge4H7KoUQH0")
        guestList = sheet.worksheet("Guestlist")
        sh = sheet.worksheet("loginTracker")
        submit = request.data
        try:
            content = ast.literal_eval(request.data['_content'])
        except:
            content = request.data
            submitGroup = content['group']
            submitName = content['firstname']
            submitFunction = content['function'] 
            peopleArray = [
             {
                 "group":submitGroup,
                 "firstName":guestList.cell(person.row,firstNameCol).value,
                 "lastName":guestList.cell(person.row,lastNameCol).value,
                 "row":person.row, 
                 "col":person.col, 
                 } 
                 for person in guestList.findall(submitGroup) if person.col == groupCol 
            ]

        if submitFunction == "login":
            loginLog(peopleArray[0],sh)
        
        if submitFunction == "rsvp":
            responsePerson = [person for person in peopleArray if person['firstName'] == submitName][0]
            guestList.update_cell(responsePerson['row'],rsvpCol,content['rsvp'])
            [sendEmail(email,password,recipient,'New RSVP!', 'New Wedding RSVP from ' + responsePerson['firstName'] + " " + responsePerson['lastName'], responsePerson['firstName'] + " " + responsePerson['lastName'] + " responded:" + content['rsvp']) for recipient in ['nate.spilman@gmail.com','csherland@yahoo.com']]
            return Response('check the doc')
        
        if submitFunction == "rsvp_rehearsal":
            responsePerson = [person for person in peopleArray if person['firstName'] == submitName][0]
            guestList.update_cell(responsePerson['row'],rehearsal_dinner_rsvp_col,content['rsvp'])
            [sendEmail(email,password,recipient,'New Rehearsal Dinner RSVP!', 'New Rehearsal Dinner RSVP from ' + responsePerson['firstName'] + " " + responsePerson['lastName'], responsePerson['firstName'] + " " + responsePerson['lastName'] + " responded:" + content['rsvp']) for recipient in ['nate.spilman@gmail.com','csherland@yahoo.com']]
            return Response('check the doc')
        
        if submitFunction == "rsvp_note":
            responsePerson = [person for person in peopleArray if person['firstName'] == submitName][0]
            guestList.update_cell(responsePerson['row'],rsvp_note_col,content['note'])
            return Response('check the doc')
        
        if submitFunction == "plus1":
            responsePerson = [person for person in peopleArray if person['firstName'] == submitName][0]
            guestList.update_cell(responsePerson['row'],plus1Col,content['plus1'])
            return Response('check the doc')
        
        if submitFunction == "food":
            responsePerson = [person for person in peopleArray if person['firstName'] == submitName][0]
            guestList.update_cell(responsePerson['row'],foodCol,content['selection'])
            return Response('check the doc')
        
        if submitFunction == "plusOneFood":
            responsePerson = [person for person in peopleArray if person['firstName'] == submitName][0]
            guestList.update_cell(responsePerson['row'],plusOneFoodCol,content['selection'])
            return Response('check the doc')
        
        if submitFunction == "email":
            responsePerson = [guestList.update_cell(person['row'],emailCol,content['email']) for person in peopleArray]
            return Response('check the doc')

        return Response({"response":'email'})

