from BSEStockQuotes import BSEStockQuotes
from CompanyDailyQuotes import CompanyDailyQuotes

class BSEDailyStockQuotes(BSEStockQuotes):

	def get_stock_quotes(self):
		for company in self.companies:
			self.stockQuotes[company] = CompanyDailyQuotes(company)

	def print_csv_output(self, delimiter=','):
		CompanyDailyQuotes.print_headers(delimiter)
		for company in self.companies:
			self.stockQuotes[company].print_info()

	def print_txt_output(self):
		CompanyDailyQuotes.print_section1_headers()
		for company in self.companies:
			self.stockQuotes[company].print_section1_info()
		CompanyDailyQuotes.print_section2_headers()
		for company in self.companies:
			self.stockQuotes[company].print_section2_info()
		CompanyDailyQuotes.print_section3_headers()
		for company in self.companies:
			self.stockQuotes[company].print_section3_info()
		CompanyDailyQuotes.print_section5_headers()
		for company in self.companies:
			self.stockQuotes[company].print_section5_info()

#Testing
"""
lstCompanyCodes = ["500180", "500209"]
st = BSEDailyStockQuotes(lstCompanyCodes)
print st.stockQuotes["500180"].face_value
for code in lstCompanyCodes:
	print st.stockQuotes[code].company_name
	print st.stockQuotes[code].stock_price
st.print_csv_output()
st.print_txt_output()
"""
