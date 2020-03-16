import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import get_money

(date, current) = get_money.get_money()
f = open('date','r')
date_prev = f.readline()
f.close()
if date_prev != date:
    f = open('date','w')
    f.write(date)
    f.close()
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


    sheet3.update_cell(2,6,current)
    sheet3.update_cell(2,8,date)

    column1 = sheet.col_values(1)
    column2 = sheet.col_values(2)
    if date not in column1:
        L = len(column2)
        print(L)
        participations = float(sheet.cell(6,5).value)
        sheet.update_cell(L+1,1,date)
        sheet.update_cell(L+1,2,"Update")
        total_money = round(participations * current, 2)
        sheet.update_cell(L+1,4, total_money)
        for row in [2,3,4,5]:
            percentage = float(sheet.cell(row,2).value)
            sheet.update_cell(row,3,total_money * percentage)
    else:
        L = len(column1)