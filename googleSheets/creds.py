
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('googleSheets/weddingWebsite.json', scope)
client = gspread.authorize(creds)