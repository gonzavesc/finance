import requests
from bs4 import BeautifulSoup
import re

url = "http://www.amundi.es/retail/product/view/LU0996179007"
ok = 0
while ok == 0:
    try:
        page = requests.get(url)
        ok = 1
    except:
        print("Not working")
html_text = page.text
html_content = page.content
f=open('out','w')
f.write(html_text)
f.close()
soup = BeautifulSoup(html_content,features='html.parser')
table = soup.find("table",class_="table-bordered-vert")
found = table.find_all("tr")
values = []
headings = []
for row in found:
    for heading in row.find_all("th"):
        headings.append(re.sub("\s","",re.sub("\n","",heading.get_text())))
for row in found[1:]:
    td_rows = row.find_all("td")
    for rows in td_rows:
        values.append(re.sub("\s","",re.sub("\n","",rows.get_text())))

print("The value at {} is {} eur".format(re.sub("A","",headings[-1]),re.sub(",",".",re.sub("EUR","",values[-2]))))
