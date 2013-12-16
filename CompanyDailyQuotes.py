#The stock data retrieved from BSEIndia website's URL is divided into various sections.
#Each section separated by the identifier '#SECTION#'
#Section1 contains company related info like company name, company's face value, scrip code and scrip ID of company
#Section2 contains basic stock info like stock price, change and percentage of change.
#Section3 contains more detailed stock info like day's high low, prev close/open, wtd price avg, total trade value, market capital, etc.
#Section4 contains Market Depth info which is not implemented here for now
#Section5 contains historical stock info like weekly high/low, monthly high/low, 52weeeks high/low, etc.


import urllib

class CompanyDailyQuotes:

  def __init__(self, company_code):

    #company_code is the scrip code of the company found in BSEIndian website
    self.company_code = company_code

    #URL Link to downloadi daily stock quotes of a company from BSEIndia website
    self.url = "http://www.bseindia.com/bseplus/StockReach/AdvStockReach.aspx?scripcode=" + company_code + "&section=tab1"

    #Parse the URL to get the various stock attributes values
    self.parse_URL()

    '''
    self.company_name = ""
    self.face_value = 0.0
    self.stock_price = 0.0
    self.change = 0.0
    self.percentage_change = 0.0
    self.day_high_low = 0.0
    self.prev_close_open = 0.0
    self.wtd_avg_price = 0.0
    self.total_traded_val = 0.0
    self.total_traded_val_unit = ""
    self.ttq_2wAvgQ = 0.0
    self.ttq_unit = ""
    self.circuit_limits = 0.0
    self.market_cap_full =0.0
    '''

  #function to parse stock data from URL
  def parse_URL(self):
    #open and read from URL
    response = urllib.urlopen(self.url)
    stockdata = response.read()

    #split into different sections
    sections = stockdata.split('#SECTION#')

    #first section contains text 'BSEPlus' followed by '#$#'
    #followed by basic company info like company name, face value, scrip code, etc.
    #the values are separated by '#@#'	
    headers = sections[0].split('#$#')
    section1_info = headers[1].split('#@#')
    self.company_name = section1_info[1]
    self.face_value = section1_info[4]

    #Second section contains basic stock info like stock price, change value, and %change
    #the values are separated by '#@#'
    section2_info = sections[1].split('#@#')
    self.stock_price = section2_info[6]
    self.change = section2_info[7]
    self.percentage_change = section2_info[8]

    #Third section contains detailed stock details
    #the values are separated by '#@#'
    section3_info = sections[2].split('#@#')
    self.day_high_low = section3_info[0]
    self.prev_close_open = section3_info[1]
    self.wtd_avg_price = section3_info[2]
    self.total_traded_val_unit = section3_info[3]
    self.total_traded_val = section3_info[4]
    self.ttq_unit = section3_info[5]
    self.ttq_2wAvgQ = section3_info[6]    
    self.circuit_limits = section3_info[7]
    self.market_cap_full = section3_info[8]

    #Fourth section contains market depth info
    #Not implemented for now

    #Fifth section contains weekly / monthly ranges info
    section5_info = sections[4].split('#@#')
    self.weekly_high = section5_info[0]
    self.weekly_low = section5_info[1]
    self.monthly_high = section5_info[2]
    self.monthly_low = section5_info[3]
    self.weeks52_high = section5_info[4]
    self.weeks52_low = section5_info[5]
    self.weeks52_high_date = section5_info[6]
    self.weeks52_low_date = section5_info[7]
    self.var_elm = section5_info[8]
    self.delivery = section5_info[9]
    self.exdate = section5_info[10]

  #print all the attributes as headers in a single line to aid in csv reports
  @staticmethod
  def print_headers(delimiter = ','):
     print "Company name" + delimiter \
     + "Face value" + delimiter \
     + "Stock price" + delimiter \
     + "Change" + delimiter \
     + "Percentage change" + delimiter  \
     + "Day's High / Low" + delimiter \
     + "Prev close / open" + delimiter \
     + "Wtd.price avg" + delimiter \
     + "Total traded value" + delimiter \
     + "TTQ / 2W Avg Q" + delimiter \
     + "Circuit limits" + delimiter \
     + "Market capital Full / Free Float (Cr.):" + delimiter \
     + "Weekly high" + delimiter \
     + "Weekly low" + delimiter \
     + "Monthly high" + delimiter \
     + "Monthly low" + delimiter \
     + "52 Weeks high" + delimiter \
     + "52 Weekls low" + delimiter \
     + "VAR / ELM % " + delimiter \
     + "Delivery " + delimiter \
     + "Exdate"

  #print all the values in a single line separated by delimiter  
  def print_info(self, delimiter = ','):
    print self.company_name + delimiter \
    + str(self.face_value) + delimiter \
    + str(self.stock_price) + delimiter \
    + str(self.change) + delimiter \
    + str(self.percentage_change) + delimiter \
    + str(self.day_high_low) + delimiter \
    + str(self.prev_close_open) + delimiter \
    + str(self.total_traded_val) + self.total_traded_val_unit + delimiter \
    + str(self.ttq_2wAvgQ) + self.ttq_unit + delimiter \
    + str(self.circuit_limits) + delimiter \
    + str(self.market_cap_full) + delimiter \
    + str(self.weekly_high) + delimiter \
    + str(self.weekly_low) + delimiter \
    + str(self.monthly_high) + delimiter \
    + str(self.monthly_low) + delimiter \
    + str(self.weeks52_high) + delimiter \
    + str(self.weeks52_high_date) + delimiter \
    + str(self.weeks52_low) + delimiter \
    + str(self.weeks52_low_date) + delimiter \
    + str(self.var_elm) + delimiter \
    + str(self.delivery) + delimiter \
    + str(self.exdate)

  #Above prints all data for each company in a single line
  #But to format the report in a better way (as a summary text file), we would need to print the data of each section separately.
  #In the below format :

  #Section1 Headers
  #Company1 Section1 data
  #Company2 Section1 data
  #....Company n Section1 data
  #Section2 Headers
  #Company1 Section2 data
  #Company2 Section2 data
  #....Company n Section2 data
  #Section3 Headers
  #Company1 Section3 data
  #Company2 Section3 data
  #....Company n Section3 data
  #Section5 Headers
  #Company1 Section5 data
  #Company2 Section5 data
  #....Company n Section5 data

  #print section-wise headers to aid in better report-formatting
  #print first section headers
  @staticmethod
  def print_section1_headers():
     print "Company name\t\t" \
     "Face value"

  #print second section headers
  @staticmethod
  def print_section2_headers():
     print "Stock price\t" \
     "Change\t" \
     "Percentage change"

  #print third section headers
  @staticmethod
  def print_section3_headers():
     print "Day's High / Low\t" \
     "Prev close / open\t" \
     "Wtd.price avg\t" \
     "Total traded value\t" \
     "TTQ / 2W Avg Q\t\t" \
     "Circuit limits\t\t" \
     "Market capital Full / Free Float (Cr.)"

  #print fifth section headers
  @staticmethod
  def print_section5_headers():
     print "Weekly high\t" \
     "Weekly low\t" \
     "Monthly high\t" \
     "Monthly low\t" \
     "52 Weeks high\t\t" \
     "52 Weeks low\t\t" \
     "VAR/ELM%\t" \
     "Delivery\t" \
     "Exdate"
 
  #print section-wise info to aid in better report formatting
  #print first section values
  def print_section1_info(self):
    print str(self.company_name).ljust(24) \
    + str(self.face_value)

  #print second section values
  def print_section2_info(self):
    print str(self.stock_price).ljust(16) \
    + str(self.change).ljust(8) \
    + str(self.percentage_change)

 #print third section values
  def print_section3_info(self):
    print str(self.day_high_low).ljust(24) \
    + str(self.prev_close_open).ljust(24) \
    + str(self.wtd_avg_price).ljust(16) \
    + (str(self.total_traded_val) + self.total_traded_val_unit).ljust(24) \
    + (str(self.ttq_2wAvgQ) + self.ttq_unit).ljust(24) \
    + str(self.circuit_limits).ljust(24) \
    + str(self.market_cap_full)

  #print fifth section values
  def print_section5_info(self):
    print self.weekly_high.ljust(16) \
    + str(self.weekly_low).ljust(16) \
    + str(self.monthly_high).ljust(16) \
    + str(self.monthly_low).ljust(16) \
    + (str(self.weeks52_high) \
    + "(" + str(self.weeks52_high_date) + ")").ljust(24) \
    + (str(self.weeks52_low) \
    + "(" + str(self.weeks52_low_date) +")").ljust(24) \
    + str(self.var_elm).ljust(16) \
    + str(self.delivery).ljust(16) \
    + str(self.exdate)

