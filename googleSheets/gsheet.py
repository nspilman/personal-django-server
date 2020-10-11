import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import json
from django.conf import settings

def create_keyfile_dict():
    variables_keys = {
        "type": os.environ.get(settings.SHEET_TYPE,"service_account"),
        "project_id": os.environ.get(settings.SHEET_PROJECT_ID,"id"),
        "private_key_id": os.environ.get(settings.SHEET_PRIVATE_KEY_ID,"key_id"),
        "private_key": os.environ.get(settings.SHEET_PRIVATE_KEY,"key"),
        "client_email": os.environ.get(settings.SHEET_CLIENT_EMAIL,"email@address.com"),
        "client_id": os.environ.get(settings.SHEET_CLIENT_ID,"sheet_id"),
        "auth_uri": os.environ.get(settings.SHEET_AUTH_URI,"URI"),
        "token_uri": os.environ.get(settings.SHEET_TOKEN_URI,"URI"),
        "auth_provider_x509_cert_url": os.environ.get(settings.SHEET_AUTH_PROVIDER_X509_CERT_URL,"CertUrl"),
        "client_x509_cert_url": os.environ.get(settings.SHEET_CLIENT_X509_CERT_URL,"CertUrl")
    }
    return variables_keys
creds = json.loads(os.environ.get('GSHEET_CONFIG'))
with open('gcreds.json', 'w') as fp:
    json.dump(creds, fp)
# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_dict('gcreds.json', scope)
client = gspread.authorize(creds)

