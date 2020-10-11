import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import json
from django.conf import settings

creds = json.loads(os.environ.get('GSHEET_CONFIG'))
with open('gcreds.json', 'w') as fp:
    json.dump(creds, fp)
# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('gcreds.json', scope)
client = gspread.authorize(creds)

