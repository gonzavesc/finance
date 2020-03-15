import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import get_money
scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
ok = 0
while ok == 0:
    try:
        creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
        ok = 1
    except:
        pass
ok = 0
while ok == 0:
    try:
        client = gspread.authorize(creds)
        ok = 1
    except:
        pass
gsh = client.open('Investing')
sheet3 = gsh.get_worksheet(2)
sheet = gsh.get_worksheet(0)

(date, current) = get_money.get_money()
sheet3.update_cell(2,6,current)
sheet3.update_cell(2,8,date)

column1 = sheet.col_values(1)

if date not in column1:
    pprint("Hey")
    L = len(column1)
    print(L)
    participations = float(sheet.cell(6,5).value)
    sheet.update_cell(L+1,1,date)
    sheet.update_cell(L+1,2,"Update")
    total_money = round(participations * current, 2)
    sheet.update_cell(L+1,4, total_money)
else:
    pprint("Not")
    L = len(column1)