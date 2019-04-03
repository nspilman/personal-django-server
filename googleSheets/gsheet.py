import gspread
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('weddingWebsite.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1IZwNQYnYAdf2Efo5YlxaMZDs3e1qtVaJge4H7KoUQH0")
guestList = sheet.worksheet("Guestlist")
spreadsheetSubmit = sheet.worksheet("spreadsheetSubmit")

# testVal =  spreadsheetSubmit.acell('A1').value
# print(testVal)
# spreadsheetSubmit.update_acell('B1', 'Bingo!')

Spilmans = guestList.findall("Spilman")
for Spilman in Spilmans:
    print(Spilman.row,Spilman.col)

list_of_lists = guestList.get_all_values()

# Extract and print all of the values
# list_of_hashes = sheet.get_all_records()
# print(list_of_hashes)