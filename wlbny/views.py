from django.shortcuts import render
import gspread
from rest_framework.response import Response
import json
from rest_framework.views import APIView
from services.googleSheets import googleSheetService

def getBusinessArray(endpoint,worksheet):
        workbook = googleSheetService.open_by_url(endpoint)
        bidness_worksheet = workbook.worksheet(worksheet)
        bidness_worksheet_values = bidness_worksheet.get_all_values()
        header = [string.lower().replace(" ", "") for string in bidness_worksheet_values[0]]
        body = bidness_worksheet_values[1:]
        bidnesses = []
        for line in body:
            bidnesses.append({header[i]:line[i] for i in range(0,len(header))})
        return bidnesses

def convertCategoryToArray(bidnesses,category):
    for bidness in bidnesses:
        bidness[category] = bidness[category].split(',')

def getSubCats(bidnesses,category):
    for bidness in bidnesses:
        subcat_name = "sub_"+category
        for value in bidness[category]:
            if "-" in value:
                value_array = value.split('-')
                bidness[subcat_name] = value_array[1].strip()
    
    for bidness in bidnesses:
        bidness[category] = [value.split('-')[0].strip() for value in bidness[category]]

def convertCategoriesToArrays(bidnesses):
        convertCategoryToArray(bidnesses,'borough')
        convertCategoryToArray(bidnesses,'typeofbusiness')
        getSubCats(bidnesses,'typeofbusiness')

class WLBNY(APIView):
    def get(self, request):
        googleSheetService.login()
        endpoint = "https://docs.google.com/spreadsheets/d/1OzCkx4MyrcEfGItwthTTIKd28aEbD3YktHUkCYVBg7w"
        worksheet = "bidnesses"
        bidnesses = getBusinessArray(endpoint, worksheet)
        convertCategoriesToArrays(bidnesses)
        return Response(bidnesses)
    
    def post(self, request):
        return Response({"PLACEHOLDER":"USE FILTER PARAMS IN POST TO RETURN FILTERED BUSINESS LIST"})
