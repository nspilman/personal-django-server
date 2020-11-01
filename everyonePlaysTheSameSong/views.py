from django.shortcuts import render
import gspread
import json
from rest_framework.response import Response
from rest_framework.views import APIView
from services.googleSheets.googleSheetService import getGoogleService

# Create your views here.
class gsheetData(APIView):
    def get(self,request):
        # googleSheetService.login()
        metadata_worksheet_name = "Metadata"
        maininfo_worksheet_name = "MainInfo"
        sheetService = getGoogleService()
        workbook = sheetService.open_by_url("https://docs.google.com/spreadsheets/d/1lZ_kEm2GtIpQgrYis7qW_GmlvnIZILf1LG16-ArWU2I")
        mainInfo = workbook.worksheet(maininfo_worksheet_name).get_all_values()
        metadata = workbook.worksheet(metadata_worksheet_name).get_all_values()
        output = []
        currentRound = 0
        for record in mainInfo:
            if record[0] == "Round":
                currentRound = int(record[1])

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
            
        # data = []
        # for record in body:
        #     output = {}
        #     for i in range(len(headers)):
        #         output[headers[i]] = record[i]
        #     data.append(output)

        # data = videosData
        return Response(output)