import get_morningstar 

def update_to_google(isin,sheet,client):
    date_file = "date_" + isin
    try:
        f = open(date_file,'r')
        date_prev = f.readline()
        f.close()
    except:
        date_prev = "00/00/0000"
    (date, current) = get_morningstar.get_morningstar(isin)
    f = open(date_file,'w')
    f.write(date)
    f.close()
    if date_prev != date:

        gsh = client.open('Finances')
        sheet= gsh.get_worksheet(sheet)
        sheet.update_cell(2,6,current)
        sheet.update_cell(2,8,date)
        max_val = float(sheet.cell(2,11).value)
        min_val = float(sheet.cell(2,13).value)
        if float(current) > max_val:
            sheet.update_cell(2,11,current)
            sheet.update_cell(2,12,date)
        if float(current) < min_val:
            sheet.update_cell(2,13,current)
            sheet.update_cell(2,14,date)
