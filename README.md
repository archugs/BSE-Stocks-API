BSE-Stocks-API
==============

An API for Indian BSE Stock Quotes

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
