import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import json
from django.conf import settings

def getGoogleService():
    creds = json.loads(os.environ.get('GSHEET_CONFIG'))
# use creds to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds, scope)
    return gspread.authorize(creds)

