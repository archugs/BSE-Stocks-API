BSE-Stocks-API
==============

An API for Indian BSE Stock Quotes

We can retrieve both daily stock quotes as well as archives of stock quotes.

Daily Stock Quotes :  
Usage :

Create an instance of BSEDailyStockQuotes by passing a list of company scrip codes as constructor argument.  
Each company in bseindia.com has a scrip code identifier.  
For example : scrip code for INFOSYS LTD. is 500209, HDFC BANK LTD. is 500180  
  
The various stock data attributes scraped from bseindia.com website are :  
company_name  
face_value  
stock_price  
change  
percentage_change  
day_high_low  
prev_close_open  
wtd_avg_price  
total_traded_val  
total_traded_val_unit  
ttq_2wAvgQ  
ttq_unit  
circuit_limits  
market_cap_full  
weekly_high  
weekly_low  
monthly_high  
monthly_low  
weeks52_high  
weeks52_high_date  
weeks52_low  
weeks52_low_date  
var_elm  
delivery  
exdate  
  
lstCodes = ["500209", "500180"]  
data = BSEDailyStockQuotes(lstCodes)  
  
To retrieve a specific attribute value:  
data.stockQuotes["500180"].company_name  
data.stockQuotes["500209"].face_value  
  
or to retrieve all companies values :  
for code in lstCodes:  
  print data.stockQuotes[code].company_name  
  print data.stockQuotes[code].stock_price  
    
To print output as csv file:  
data.print_csv_output()  
  
To print output as text summary report:  
data.print_txt_output()  


Archived Stock Quotes :   
Usage : 
 
Create an instance of BSEArchivedStockQuotes by passing a list of company scrip codes as constructor argument.  
Each company in bseindia.com has a unique scrip code identifier.  
For example : scrip code for INFOSYS LTD. is 500209, HDFC BANK LTD. is 500180   
   
The various attributes of archived stock data scraped from bseindia.com website are :   
companyname  
date  
open_price   
day_high   
day_low   
close_price  
wap  
no_of_shares  
no_of_trades  
total_turnover   
deliverable_qty  
percent_qty  
highlow_spread   
closeopen_spread  
  
lstCodes = ["500209", "500180"]  
data = BSEArchivedStockQuotes(lstCodes)  
  
To retrieve a specific attribute value:  
data.stockQuotes["500180"].company_name  
data.stockQuotes["500180"].open_price[0]  
data.stockQuotes["500209"].total_turnover[5]  

or to retrieve all archived values over the period  
for i in range(1, len(data.stockQuotes["500180"].date)):  
	print data.stockQuotes["500180"].no_of_shares[i]  
	print data.stockQuotes["500180"].no_of_trades[i]  
  
or to retrieve all companies values :  
for code in lstCodes:  
  for i in range(1, len(data.stockQuotes[code].date)):  
    print data.stockQuotes[code].day_high[i]  
    print data.stockQuotes[code].day_low[i]  
    
To print entire output:  
data.print_output()   
  
We can also print the output separated by other delimiters:  
data.print_output("|")  
