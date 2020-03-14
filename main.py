import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import get_money
scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
client = gspread.authorize(creds)
gsh = client.open('Investing')
sheet3 = gsh.get_worksheet(2)
sheet = gsh.get_worksheet(0)

(date, current) = get_money.get_money()
sheet3.update_cell(2,6,current)
sheet3.update_cell(2,8,date)

# table = sheet.get_all_records()

# pprint(table)

# row = sheet.row_values(3)

# pprint(row)

# column = sheet.col_values(3)

# pprint(column)

# cell = sheet.cell(6,5).value

# pprint(cell)

