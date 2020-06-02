import requests
from bs4 import BeautifulSoup
import re
import calendar

months = {}
for item in enumerate(calendar.month_abbr):
    months[item[1]] = item[0]
def get_morningstar(isin):
    url = "https://quotes.morningstar.com/fund/c-header?t=" + isin
    page = requests.get(url)
    content = page.content
    parsed_html = BeautifulSoup(content, features='html.parser')
    table = parsed_html.find("div", {"class" : "gr_colm_d1c"})
    value = re.search(r'[0-9]{1,}\.[0-9]{1,2}',table.get_text())
    date = re.search(r'[0-9]{1,2} [a-zA-Z]{3} [0-9]{4}',parsed_html.get_text())
    date = date.group(0)
    value = value.group(0)
    month = re.search(r'[a-zA-Z]{3}',date)
    month = month.group(0)
    month = int(months[month])
    day = re.search(r'[0-9]{1,2}',date)
    day = int(day.group(0))
    year = re.search(r'[0-9]{4}',date)
    year = int(year.group(0))
    date = "{:02d}/{:02d}/{:04d}".format(day,month,year)
    return date, value
