import gspread
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://docs.google.com/spreadsheets/d/1qj66WOF9XEMrXjBgHeoR5grXFi0vzh2nH74aqqITE94/edit#gid=0',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('even-dream-331809-e915b10b7783.json', scope)
gc = gspread.authorize(credentials)
wks = gc.open('excelRoster').sheet1

wks.update_acell('A1', 'Hello World!')
print(wks.acell('A1'))
