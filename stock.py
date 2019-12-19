import requests
from bs4 import BeautifulSoup
import re
import math

##### iterate every page #######
def getpage(pageurl, sector):
  page=requests.get(pageurl)
  soup=BeautifulSoup(page.content, 'html.parser')

  rows = soup.find("table").find("tbody").find_all("tr")

  #print(rows)

  for i in rows:
    #print(i)
    #print("=============================\n")
    cells = i.find_all("td")
    c0 = cells[0].get_text()  #symbol
    c1 = cells[1].get_text()  #company name
    c2 = cells[2].get_text()  #price
    c3 = cells[3].get_text()  #price change
    c4 = cells[4].get_text()  #price change percent
    c5 = cells[5].get_text()  #vol
    c6 = cells[6].get_text()  #3 mon vol
    c7 = cells[7].get_text()  #MarketCap
    c8 = cells[8].get_text()  #PE Ratio

    print(c0+"\t"+c1+"\t"+c2+"\t"+c3+"\t"+c4+"\t"+c5+"\t"+c6+"\t"+c7+"\t"+c8+"\t"+sector)


#### starting from here #######
tup = ("basic_materials", "communication_services", "consumer_cyclical", "consumer_defensive", "energy", "financial_services", "healthcare", "industrials", "real_estate", "technology", "utilities")
#tup = ("basic_materials", "communication_services")
for i in tup:
  x="https://finance.yahoo.com/sector/ms_"+i+"?offset=0&count=100"
  #print(x)
    
  page=requests.get(x)
  soup=BeautifulSoup(page.content, 'html.parser')

  #1-100 of 149 result
  r1=0      #1
  r2=0      #100
  total=0   #149
  test=soup.find_all("span")
  for j in test:
    x0=j.get_text()

    if re.search("(\d+)-\d+ of \d+", x0):  
      mRegex = re.compile(r'(\d+)-(\d+) of (\d+) result') #1-100 of 149 result
      mo = mRegex.search(x0) 
      r1=mo.group(1)
      r2=mo.group(2)
      total=mo.group(3)
    
 # print(r1)        
 # print(r2)
 # print(total)
  pnum=int(total)/100   #1.49
  pnum=(int)(math.ceil(pnum))  #2 ceil(1.49)=2
 # print(pnum)
      
  for k in range(pnum):
    pageurl="https://finance.yahoo.com/sector/ms_"+i+"?offset="+str(k*100)+"&count=100"
    getpage(pageurl, i)


