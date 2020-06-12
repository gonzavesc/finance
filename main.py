import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import get_money
import get_bitcoin
import datetime
import update_to_google
comission = 0.975
bit_value = get_bitcoin.get_btc()
(date, current) = get_money.get_money()
f = open('date','r')
date_prev = f.readline()
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
if date_prev != date:
    f = open('date','w')
    f.write(date)
    f.close()
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
        sheet.update_cell(L+1,9, current)
        for row in [2,3,4,5]:
            percentage = float(column2[row - 1])
            sheet.update_cell(row,3,total_money * percentage)
    else:
        L = len(column1)
    #setting highest number
    max_val = float(sheet3.cell(2,11).value)
    min_val = float(sheet3.cell(2,13).value)
    if float(current) > max_val:
        sheet3.update_cell(2,11,current)
        sheet3.update_cell(2,12,date)
    if float(current) < min_val:
        sheet3.update_cell(2,13,current)
        sheet3.update_cell(2,14,date)
    
    #Updateting for finances sheet 
    gsh = client.open('Finances')
    sheet2 = gsh.get_worksheet(1)
    sheet2.update_cell(2,6,current)
    sheet2.update_cell(2,8,date)
    max_val = float(sheet2.cell(2,11).value)
    min_val = float(sheet2.cell(2,13).value)
    if float(current) > max_val:
        sheet2.update_cell(2,11,current)
        sheet2.update_cell(2,12,date)
    if float(current) < min_val:
        sheet2.update_cell(2,13,current)
        sheet2.update_cell(2,14,date)
gsh = client.open('Finances')
sheet3 = gsh.get_worksheet(2)
bit_value = float(bit_value) * comission
sheet3.update_cell(2,6,bit_value)
y = datetime.datetime.now().year
m = datetime.datetime.now().month
d = datetime.datetime.now().day
date = "{:02}/{:02}/{:04}".format(d,m,y)
sheet3.update_cell(2,8,date)
max_val = float(sheet3.cell(2,11).value)
min_val = float(sheet3.cell(2,13).value)
if float(bit_value) > max_val:
    sheet3.update_cell(2,11,bit_value)
    sheet3.update_cell(2,12,date)
if float(bit_value) < min_val:
    sheet3.update_cell(2,13,bit_value)
    sheet3.update_cell(2,14,date)
#Now we update the other isin
sheet=gsh.get_worksheet(3)
update_to_google.update_to_google("ES0110407097",3,client)

