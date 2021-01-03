from django.shortcuts import render
import gspread
import json
from rest_framework.response import Response
from rest_framework.views import APIView
from services.googleSheets.googleSheetService import getGoogleService

# Create your views here.

class CurrentState(APIView):
    def get(self,request):
        state_worksheet_name = "State"
        sheetService = getGoogleService()
        workbook = sheetService.open_by_url("https://docs.google.com/spreadsheets/d/1lZ_kEm2GtIpQgrYis7qW_GmlvnIZILf1LG16-ArWU2I")
        state = workbook.worksheet(state_worksheet_name).get_all_values()
        output = {row[0]:row[1] for row in state}
        return Response(output)
        # currentRound = [record[1] for record in metadata if record[0] == roundKey][0]
        # currentPhase = [record[1] for record in metadata if record[0] == currentPhaseKey][0]
        # mailingList = [record[1] for record in metadata if record[0] == signupSheetKey][0]
        # signupSheet = [record[1] for record in metadata if record[0] == signupSheetKey][0]
        # output = {
        #         "round":currentRound,
        #         "phase":currentPhase,
        #         "mailingList":mailingList,
        #         "signupSheet": signupSheet
        #          }
        # return Response(output)

class RoundsMetaData(APIView):
    def get(self,request, roundId = None):
        # googleSheetService.login()
        metadata_worksheet_name = "Metadata"
        maininfo_worksheet_name = "MainInfo"
        roundKey = "Round"
        sheetService = getGoogleService()
        workbook = sheetService.open_by_url("https://docs.google.com/spreadsheets/d/1lZ_kEm2GtIpQgrYis7qW_GmlvnIZILf1LG16-ArWU2I")
        mainInfo = workbook.worksheet(maininfo_worksheet_name).get_all_values()
        metadata = workbook.worksheet(metadata_worksheet_name).get_all_values()
        output = []
        currentRound = 0
        currentRound = [int(record[1]) for record in mainInfo if record[0]== roundKey][0]

        for i in range(1,currentRound + 1):
            round = i
            title = ''
            playlist = '<div/>'
            image = ''
            for record in metadata:
                if record[0] == f"{i}_title":
                    title = record[1]
                if record[0] == f"{i}_playlist":
                    playlist = record[1]
                if record[0] == f"{i}_image":
                    image = record[1]
            output.append({"round":round,"title":title,"playlist":playlist, "image": image})
        if roundId != None:
            output = [record for record in output if record['round'] == int(roundId)]
            
        # data = []
        # for record in body:
        #     output = {}
        #     for i in range(len(headers)):
        #         output[headers[i]] = record[i]
        #     data.append(output)

        # data = videosData
        return Response(output)