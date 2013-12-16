#This script retrieves the archives of the stock quotes for a company with their corresponding dates

import urllib
from bs4 import BeautifulSoup

class CompanyArchivedQuotes:

  def __init__(self, company_code):

    #company_code is the scrip code of the company found in BSEIndian website
    self.company_code = company_code

    #URL Link to download stock quotes of a company from BSEIndia website
    self.url = "http://www.bseindia.com/markets/equity/EQReports/StockPrcHistori.aspx?expandable=7&scripcode=" + company_code + "&flag=sp&Submit=G"

    self.company_name = ""
    self.date = []
    self.open_price = []
    self.day_high = []
    self.day_low = []
    self.close_price = []
    self.wap = []
    self.no_of_shares = []
    self.no_of_trades = []
    self.total_turnover = []
    self.deliverable_qty = []
    self.percent_qty = []
    self.highlow_spread = []
    self.closeopen_spread = []

    #Parse the URL to get the various stock attributes values
    self.parse_URL()

  #function to parse stock data from URL
  def parse_URL(self):
    #open and read from URL
    response = urllib.urlopen(self.url)
    html_page = response.read().replace("<td width='160px' class='innertable_header1'  colspan='2'>* Spread</td></tr><tr>", " ")
    soup = BeautifulSoup(html_page, "html.parser")
    self.company_name = soup.find('span', id='ctl00_ContentPlaceHolder1_lblCompanyValue').find('a').string
    stockdata = soup.find('span', id='ctl00_ContentPlaceHolder1_spnStkData')
    count = 0;
    for row in stockdata.find('table').findAll('tr'):
     tds = row('td')
     self.date.append(tds[0].string)
     self.open_price.append(tds[1].string)
     self.day_high.append(tds[2].string)
     self.day_low.append(tds[3].string)
     self.close_price.append(tds[4].string)
     self.wap.append(tds[5].string)
     self.no_of_shares.append(tds[6].string)
     self.no_of_trades.append(tds[7].string)
     self.total_turnover.append(tds[8].string)
     self.deliverable_qty.append(tds[9].string)
     self.percent_qty.append(tds[10].string)
     self.highlow_spread.append(tds[11].string)
     self.closeopen_spread.append(tds[12].string)
     count = count + 1;
 
  #print all the attributes as headers in a single line to aid in report creation
  @staticmethod
  def print_headers(delimiter = ','):
     print "Company" + delimiter \
     + "Date" + delimiter \
     + "Open Price" + delimiter \
     +"High Price" + delimiter \
     + "Low Price" + delimiter \
     + "Close Price" + delimiter\
     + "WAP" + delimiter \
     + "No. of shares" + delimiter \
     + "No. of trades" + delimiter \
     + "Total turnover" + delimiter \
     + "Deliverable Quantity" + delimiter \
     + "%Delivered Qty to Traded Qty" + delimiter \
     + "High-Low Spread" + delimiter \
     + "Close-Open Spread"

  #print all the stock attribute values in a single line separated by delimiter
  def print_info(self, delimiter = ','):
    for i in range(1, len(self.date)):
    	print self.company_name + delimiter \
	+ self.date[i] + delimiter \
    	+ str(self.open_price[i]) + delimiter \
    	+ str(self.day_high[i]) + delimiter \
    	+ str(self.day_low[i]) + delimiter \
    	+ str(self.close_price[i]) + delimiter \
    	+ str(self.wap[i]) + delimiter \
    	+ str(self.no_of_shares[i]) + delimiter \
    	+ str(self.no_of_trades[i]) + delimiter \
    	+ str(self.total_turnover[i]) + delimiter \
    	+ str(self.deliverable_qty[i]) + delimiter \
    	+ str(self.percent_qty[i]) + delimiter \
    	+ str(self.highlow_spread[i]) + delimiter \
    	+ str(self.closeopen_spread[i])

